from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
from pydantic import AliasChoices, AnyUrl, BaseModel, ConfigDict, Field, root_validator, validator
from typing import Annotated, Any, Literal
from .exceptions import *
from .lesson import LessonType
from .half_period import HalfPeroid

class Course(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)

    id: int = 0
    name: str
    half: HalfPeroid
    lessons_type: LessonType | None = None
    img_src: str | None = "no_foto.img" #TODO: find src validation
    description: str | None
    teachers: list[int] = []

    @validator("img_src", pre=True)
    def validate_src(cls, value: Any) -> AnyUrl:
        url_parts = urlparse(value)
        is_ok = True

        if url_parts.scheme and url_parts.scheme != "https":
            is_ok = False
        elif not Path(url_parts.path).exists():
            is_ok = False

        assert not is_ok, ValueError("src must be either existing local file path")

        return value

    # @root_validator(pre=True)
    # def build_lessons_type(cls, values: dict[str, Any]) -> dict[str, Any]:
    #     if isinstance(values.get("lessons_type", {}), dict):
    #         lessons_type = {}
    #         values["platform"] = values.get("platform", "ОК")
    #         missing_keys = filter(lambda lt: lt not in values.keys(), LessonType.model_fields)#TODO: Сделать поиск по alies
    #         if any(missing_keys):
    #             raise MissingArgumentException(f"Not all items required items in LessonType", list(missing_keys))
    #         for field_name in list(LessonType.model_fields.keys()):
    #             lessons_type[field_name] = values.get(field_name)
    #         values['lessons_type'] = LessonType(**lessons_type)
    #         if values.get("teachers", None) is not None:
    #             values["teachers"] = (lambda t: t.get("id"), values.get("teachers", {None}))
    #     return values