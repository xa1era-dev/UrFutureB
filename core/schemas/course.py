from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
from pydantic import AnyUrl, BaseModel, ConfigDict, Field, root_validator, validator
from typing import Annotated, Any, Literal
from .exceptions import *


class LessonsType(BaseModel):
    Type: Annotated[str, Literal["online", "traditional", "mixed"]] = Field(alias="course_type") 
    owner: str = Field(default="УрФУ", alias="created_by")
    platform: str | None = Field(default=None) #"ОК", "elearn", "ulear"... Только если online

    @validator("Type")
    def validate_platform(cls, v: Annotated[str, Literal["online", "traditional", "mixed"]]):
        if v != "online":
            cls.platform = None
        return v
    
    model_config = ConfigDict(extra='ignore', from_attributes=True)

class Course(BaseModel):
    name: str
    year: int = Field(ge=2024)
    half: Literal[1, 2] = 1
    lessons_type: LessonsType | None = None
    img_src: str = "no_foto.img" #TODO: find src validation
    description: str 
    teachers: list[int] | None

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

    @root_validator(pre=True)
    def build_lessons_type(cls, values: dict[str, Any]) -> dict[str, Any]:
        if isinstance(values.get("lessons_type", {}), dict):
            lessons_type = {}
            values.get("platform", "ОК")
            missing_keys = filter(lambda lt: lt not in values.keys(), LessonsType.model_fields.keys())
            if any(missing_keys):
                raise MissingArumentException(f"Not all items required items in LessonType", list(missing_keys))
            for field_name in list(LessonsType.model_fields.keys()):
                lessons_type[field_name] = values.get(field_name)
            cls.lessons_type = LessonsType(**lessons_type)
            if values.get("teachers", None) is not None:
                values["teachers"] = (lambda t: t.get("id"), values.get("teachers", {None}))
        return values
    
    model_config = ConfigDict(extra='ignore', from_attributes=True)