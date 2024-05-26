import json
from fastapi import FastAPI, Request, Response, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_csrf_protect.exceptions import CsrfProtectError
from api.v1 import api
from api.v1.responses import *
from login import loginrouter
from core.schemas import TUPLES_ERR_EXC
from core.schemas.responses import *

app = FastAPI(
    version="0.3.0dev"
)

app.include_router(api.apiv1router)
app.include_router(loginrouter)

app.mount("/static", StaticFiles(directory="static/public", html=True), name="static")
templates = Jinja2Templates(directory="static/public")

@app.exception_handler(NotFoundApiException)
async def not_found_handler(r: Request, exc: NotFoundApiException):
    return JSONResponse(
        status_code=NotFoundApiError._code.default, # type: ignore
        content=jsonable_encoder(NotFoundApiError(**exc.__dict__))
    )

@app.exception_handler(MissingArgumentException)
async def missing_arguments(r: Request, exc: MissingArgumentException):
    return JSONResponse(
        status_code=MissingArgumetsError._code.default, # type: ignore
        content=jsonable_encoder(MissingArgumetsError(**exc.__dict__))
    )

@app.exception_handler(UnauthorizedApiException)
async def user_not_authorizated(r: Request, exc: UnauthorizedApiException):
    return JSONResponse(
        status_code=UnauthorizedApiError._code.default, # type: ignore
        content=jsonable_encoder(UnauthorizedApiError(**exc.__dict__))
    )

@app.exception_handler(NotImplementedException)
async def endpoint_is_not_implemented(r: Request, exc: NotImplementedException):
    return JSONResponse(
        status_code=NotImplementError._code.default, # type: ignore
        content=jsonable_encoder(NotImplementError(**exc.__dict__))
    )

@app.exception_handler(CsrfProtectError) # type: ignore
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(name="index.html", request=request)
