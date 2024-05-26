from typing import Annotated, Literal
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, field_serializer, model_serializer, validator
from .lesson_time import LessonTime
from ..enums import LessonType as EnumLessonType

class LessonType(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)
    type: Annotated[EnumLessonType, Field(default=EnumLessonType.PRACTICE)]
    owner: str = Field(default="УрФУ", validation_alias=AliasChoices("owner", "created_by"))
    platform: str | None = Field(default=None) #"ОК", "elearn", "ulear"... Только если online
    kabinet: str | None = Field(default=None) #Р-123 Для traditional

    @validator("type")
    def validate_platform(cls, v: Annotated[str, Literal["online", "traditional", "mixed"]]):
        if v != EnumLessonType.OK.value:
            cls.platform = None
        else:
            cls.kabinet = None
        return v
    
    @field_serializer("type")
    def serialize_group(self, type: EnumLessonType, _info):
        return type.value


class Lesson(LessonTime, LessonType):
    ...