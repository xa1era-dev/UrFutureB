from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel
from pydantic_settings import BaseSettings
import os
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

@loginrouter.get("/login")
def form(request: Request, csrf_protect: CsrfProtect = Depends()):
    csrf_token, signed_token = csrf_protect.generate_csrf_tokens()
    response = JSONResponse(
        {"signed_token": signed_token, "csrf_token": csrf_token}
    )
    csrf_protect.set_csrf_cookie(signed_token, response)
    return response

@loginrouter.post("/login", response_class=JSONResponse)
async def create_post(request: Request, csrf_protect: CsrfProtect = Depends()):
    """
    Creates a new Post
    """
    await csrf_protect.validate_csrf(request)
    response: JSONResponse = JSONResponse(status_code=200, content={"detail": "OK"})
    csrf_protect.unset_csrf_cookie(response)  # prevent token reuse
    return response