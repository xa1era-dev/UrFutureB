import json
from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from api.v1 import api
from api.v1.responses import *

app = FastAPI(
    version="0.2dev"
)

app.include_router(api.apiv1router)

@app.exception_handler(NotFoundApiException)
async def not_found_handler(r: Request, exc: NotFoundApiException):
    return JSONResponse(
        status_code=404,
        content={"msg": exc.msg}
    )

@app.exception_handler(MissingArumentException)
async def missing_arguments(r: Request, exc: MissingArumentException):
    return JSONResponse(
        status_code=520,
        content=dict(msg=exc.message, keys=exc.arguments)
    )

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTMLResponse("Index.html")


@app.get("/test/{item_id}")
def test_desc(response: Response, item_id: int, q: str | None = None) -> dict[str, str]:
    # response.status_code = 201
    return {"msg":"sdgdsg"}