from pydantic import BaseModel

class NotFoundApiError(BaseModel):
    message: str

class MissingArgumetsError(BaseModel):
    message: str
    keys: list[str]