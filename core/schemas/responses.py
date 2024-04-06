from pydantic import BaseModel

class NotFoundApiError(BaseModel):
    msg: str | None = None