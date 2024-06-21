from datetime import datetime, timedelta, timezone
import email
import jwt
from typing import Annotated, Union
from fastapi import APIRouter, Depends, HTTPException, Request, status
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from core.models.database import DB_URL, create_session
from core.models.user import User



SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7dfgdfgh"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 180



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login",
                                     scopes={
                                        "urfuture": "UrFuture",
                                        "procompentecies": "ПроКомпетенции2.0"
                                     })

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

class TokenUser(BaseModel):
    user: str
    psw: str

async def get_authorized_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        username: str = payload.get("user")
        password: str = payload.get("psw")
        if username is None or password is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    return token

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_user(username):
    with create_session(DB_URL) as sess:
        user = sess.query(User).where(User.username == username).first()
        return user

async def add_user(username, password):
    with create_session(DB_URL) as sess:
        print(get_password_hash(password))
        user = User(username=username, password=get_password_hash(password), email="", image_src="")
        sess.add(user)

async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


