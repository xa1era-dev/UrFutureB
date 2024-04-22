from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from api.v1 import api
from api.v1.responses import *

app = FastAPI(
    version="0.1dev"
)

app.include_router(api.apiv1router)

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