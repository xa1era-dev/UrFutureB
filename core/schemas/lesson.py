from typing import Annotated, Literal
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, model_serializer, validator
from .lesson_time import LessonTime
from ..enums import LessonType as EnumLessonType

class LessonType(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)
    type: EnumLessonType
    owner: str = Field(default="УрФУ", validation_alias=AliasChoices("owner", "created_by"))
    platform: str | None = Field(default=None) #"ОК", "elearn", "ulear"... Только если online
    kabinet: str | None = Field(default=None) #Р-123 Для traditional

    @validator("type")
    def validate_platform(cls, v: Annotated[str, Literal["online", "traditional", "mixed"]]):
        if v != "online":
            cls.platform = None
        if v != "traditional":
            cls.kabinet = None
        return v


class Lesson(LessonTime, LessonType):
    ...