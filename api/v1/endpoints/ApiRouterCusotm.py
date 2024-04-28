import types
from typing import Callable, Iterable
from fastapi import APIRouter
from fastapi.types import DecoratedCallable
from pydantic import BaseModel
from core.schemas import SCHEMA_ERRORS_LIST
from ..responses import api_responses

class ApiRouterCustom(APIRouter):
    _check_authoriztion: bool = False

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def api_route(self, *args, **kwargs) -> Callable[[DecoratedCallable], DecoratedCallable]:
        models_raw = kwargs.get("response_model", [])
        if (isinstance(models_raw, types.UnionType)):
            models_raw = getattr(models_raw, "__args__", ())
        else:
            models_raw = tuple([models_raw])

        models = set(models_raw) & set(SCHEMA_ERRORS_LIST)
        codes = self._models_to_codes(models)
        if (not self._check_authoriztion and 401 in codes):
            codes.remove(401)
        responses = dict((key, api_responses.get(key, {})) for key in codes)
        kwargs["responses"] = responses
        self._check_authoriztion = False
        #TODO: Поиск ошибок в моделях pydantic и добавление к схемам ответа
        return super().api_route(*args, **kwargs)
    
    def _models_to_codes(self, models: Iterable[BaseModel]) -> list[int]:
        return [200, *map(lambda m: m._code.default, models)] # type: ignore
    
    def check_autorization(self): #role: Literal[*enum], platform: Literal[*enum]
        self._check_authoriztion = True
        def decorator(f):
            return f
        return decorator