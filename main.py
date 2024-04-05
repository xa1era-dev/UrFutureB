from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from api.v1 import api

app = FastAPI(
    version="0.1dev"
)

app.include_router(api.route)


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