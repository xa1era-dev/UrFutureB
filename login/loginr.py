from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_csrf_protect import CsrfProtect
from fastapi_login import LoginManager
from pydantic import BaseModel
from pydantic_settings import BaseSettings
import hashlib
from core.models import Session, create_session, DB_URL, User
from dotenv import load_dotenv

load_dotenv(r"c:\Users\IEBul\OneDrive\UrFuture\envvars\db.env")

loginrouter = APIRouter()

class CsrfSettings(BaseSettings):
    secret_key: str = "testtoken"
    cookie_samesite: str = "none"
    cookie_secure: bool = True
    max_age: int = 30

def get_csrf_config():
    return CsrfSettings()

CsrfProtect.load_config(settings=get_csrf_config) # type: ignore

SECRET = 'your-secret-key'

manager = LoginManager(SECRET, token_url='/auth/token')

@loginrouter.get("/csrf")
def form(request: Request, csrf_protect: CsrfProtect = Depends()):
    csrf_token, signed_token = csrf_protect.generate_csrf_tokens()
    response = JSONResponse(
        {"csrf_token": csrf_token}
    )
    csrf_protect.set_csrf_cookie(signed_token, response)
    return response

@loginrouter.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    with create_session(DB_URL) as sess:
        user = sess.query(User).where((User.email==email) | (User.username==email)).first()
        if not user:
            raise InvalidCredentialsException  # you can also use your own HTTPException
        elif hashlib.md5(password.encode()) != user.password:
            raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=email)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

# @loginrouter.post("/login", response_class=JSONResponse)
# async def create_post(request: Request, csrf_protect: CsrfProtect = Depends()):
#     """
#     Creates a new Post
#     """
#     await csrf_protect.validate_csrf(request)
#     response: JSONResponse = JSONResponse(status_code=200, content={"detail": "OK"})
#     csrf_protect.unset_csrf_cookie(response)  # prevent token reuse
#     return response