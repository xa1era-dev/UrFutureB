import json
from fastapi import FastAPI, Request, Response, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from api.v1 import api
from api.v1.responses import *
from core.schemas import TUPLES_ERR_EXC
from core.schemas.responses import *

app = FastAPI(
    version="0.2.1dev"
)

app.include_router(api.apiv1router)

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

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTMLResponse("Index.html")


@app.get("/test/{item_id}")
def test_desc(response: Response, item_id: int, q: str | None = None) -> dict[str, str]:
    # response.status_code = 201
    return {"msg":"sdgdsg"}