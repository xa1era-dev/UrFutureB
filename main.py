from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from api.v1 import api
from api.v1.responses import *

app = FastAPI(
    version="0.1dev"
)

from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from pydantic import BaseModel

class CsrfSettings(BaseModel):
    secret_key: str = "testtoken"
    cookie_samesite: str = "none"
    cookie_secure: bool = True
    max_age: int = 30

@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()

@app.get("/login")
def form(request: Request, csrf_protect: CsrfProtect = Depends()):
    """
    Returns form template.
    """
    csrf_token, signed_token = csrf_protect.generate_csrf_tokens()
    response = JSONResponse(
        {"signed_token": signed_token, "csrf_token": csrf_token}
    )
    csrf_protect.set_csrf_cookie(signed_token, response)
    return response

@app.post("/login", response_class=JSONResponse)
async def create_post(request: Request, csrf_protect: CsrfProtect = Depends()):
    """
    Creates a new Post
    """
    await csrf_protect.validate_csrf(request)
    response: JSONResponse = JSONResponse(status_code=200, content={"detail": "OK"})
    csrf_protect.unset_csrf_cookie(response)  # prevent token reuse
    return response

@app.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

app.include_router(api.route)

@app.exception_handler(NotFoundApiException)
async def not_found_handler(r: Request, exc: NotFoundApiException):
    return JSONResponse(
        status_code=404,
        content={"msg": exc.msg}
    )

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTMLResponse("Index.html")


@app.get("/test/{item_id}", responses={
    200: {
        "description": "Found",
        "content": {
            "application/json": {
                "example": {"id": "bar", "value": "The bar tenders"}
            }
        },
    }, 
    201: {
        "description": "Test desc for 201",
        "content": {
            "text/html": {
                "example" : "<html></html>"
            }
        },
    }, 
})
def test_desc(response: Response, item_id: int, q: str | None = None) -> dict[str, str]:
    # response.status_code = 201
    return {"msg":"sdgdsg"}