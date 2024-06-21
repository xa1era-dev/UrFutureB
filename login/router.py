from datetime import datetime, timedelta, timezone
from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from pydantic import BaseModel

import login
from .settings import LoginCSRF, AccessCSRF
from core.models import create_session, DB_URL, User
from .schemas.token import Token
from .depends import authenticate_user, create_access_token, get_authorized_user, add_user

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7dfgdfgh"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 180

loginrouter = APIRouter()

# @loginrouter.get("/csrf")
# async def form(request: Request, csrf_protect: AccessCSRF = Depends()):
#     csrf_token, signed_token = csrf_protect.generate_csrf_tokens()
#     print(csrf_protect._max_age)
#     response = JSONResponse(
#         {"csrf_token": csrf_token}
#     )
#     csrf_protect.set_csrf_cookie(signed_token, response)
#     return response

@loginrouter.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"user": user.username, "psw": user.password}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@loginrouter.post("/me")
async def test_me(user: Annotated[User, Depends(get_authorized_user)]):
    return "me"

@loginrouter.post("/register")
async def register(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await authenticate_user(form_data.username, form_data.password)
    if user:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="User is registered",
            headers={"WWW-Authenticate": "Bearer"},
        )
    await add_user(form_data.username, form_data.password)