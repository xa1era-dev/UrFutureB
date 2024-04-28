from typing import Literal
from pydantic import BaseModel, PrivateAttr
from .exceptions import *

class NotFoundApiError(BaseModel):
    _code: int = 404
    _exc: type[Exception] = NotFoundApiException
    message: str

class MissingArgumetsError(BaseModel):
    _code: int = 520
    _exc: type[Exception] = MissingArgumentException
    message: str
    arguments: list[str]

class UnauthorizedApiError(BaseModel):
    _code: int = 401
    _exc: type[Exception] = UnauthorizedApiException
    message: str
    platform: Literal["UrFuture", "ПроКомпетенции2.0"]

class NotImplementError(BaseModel):
    _code: int = 501
    _exc: type[Exception] = NotImplementedException
    message: str
