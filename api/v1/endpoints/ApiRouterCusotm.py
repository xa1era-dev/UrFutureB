import types
from typing import Callable, Iterable, Literal
from fastapi import APIRouter
from fastapi.types import DecoratedCallable
from pydantic import BaseModel
from core.schemas import SCHEMA_ERRORS_LIST
from core.enums.user_roles import UserRoles
from ..responses import api_responses

class ApiRouterCustom(APIRouter):

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
        if (401 in codes):
            codes.remove(401)
        responses = dict((key, api_responses.get(key, {})) for key in codes)
        kwargs["responses"] = responses
        #TODO: Поиск ошибок в моделях pydantic и добавление к схемам ответа
        return super().api_route(*args, **kwargs)
    
    def _models_to_codes(self, models: Iterable[BaseModel]) -> list[int]:
        return [200, *map(lambda m: m._code.default, models)] # type: ignore
