from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from pydantic import BaseModel
from .settings import LoginCSRF, AccessCSRF
from core.models import create_session, DB_URL, User

loginrouter = APIRouter()

@loginrouter.get("/csrf")
async def form(request: Request, csrf_protect: AccessCSRF = Depends()):
    csrf_token, signed_token = csrf_protect.generate_csrf_tokens()
    print(csrf_protect._max_age)
    response = JSONResponse(
        {"csrf_token": csrf_token}
    )
    csrf_protect.set_csrf_cookie(signed_token, response)
    return response

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login",
                                     scopes={
                                        "urfuture": "UrFuture",
                                        "procompentecies": "ПроКомпетенции2.0"
                                     })

class User(BaseModel):
    name: str
    password: str

async def get_user(token: Annotated[str, Depends(oauth2_scheme)]):
    print(token)
    return token

@loginrouter.get("/me")
async def get_auth_user(request: Request, user: Annotated[User, Depends(get_user)], csrf_protect: AccessCSRF = Depends()):
    print(request)
    await csrf_protect.validate_csrf(request)
    return user

class CSRF(BaseModel):
    csrf: str

@loginrouter.post('/login')
async def login(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print(data.__dict__)
    return {"dfsd": uuid.uuid4(), "token_type": "bearer", "role": "dev"}
    # await csrf_protect.validate_csrf(request)
    # email = data.username
    # password = data.password

    # with create_session(DB_URL) as sess:
    #     user = sess.query(User).where((User.email==email) | (User.username==email)).first()
    #     if not user:
    #         raise InvalidCredentialsException  # you can also use your own HTTPException
    #     elif hashlib.md5(password.encode()) != user.password:
    #         raise InvalidCredentialsException

    # access_token = manager.create_access_token(
    #     data=dict(sub=email)
    # )
    # response = JSONResponse(status_code=200, content={'access_token': access_token, 'token_type': 'bearer'})
    # csrf_protect.unset_csrf_cookie(response)
    # return response

@loginrouter.post("/register", response_class=JSONResponse)
async def create_post(request: Request, data: OAuth2PasswordRequestForm = Depends(), csrf_protect: LoginCSRF = Depends()):
    await csrf_protect.validate_csrf(request)
    email = data.username
    password = data.password
    response: JSONResponse = JSONResponse(status_code=200, content={"detail": "OK"})
    csrf_protect.unset_csrf_cookie(response)  # prevent token reuse
    with create_session(DB_URL) as sess:
        user = sess.query(User).where((User.email==email) | (User.username==email)).first()
        if not user:
            user = User(email=email, password=password)
            sess.add(user)
            sess.commit()
    return response