from typing import Annotated, Literal
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, field_serializer, model_serializer, validator

from .teacher import Teacher
from .lesson_time import LessonTime
from ..enums import LessonType as EnumLessonType

class Lesson(LessonTime):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)
    
    type: Annotated[EnumLessonType, Field(default=EnumLessonType.PRACTICE)] = EnumLessonType.PRACTICE
    owner: str = Field(default="УрФУ", validation_alias=AliasChoices("owner", "created_by"))
    place: str | None = Field(default=None) # Общее поле для platform и kabinet
    teachers: list[Teacher] = []
    
    @field_serializer("type")
    def serialize_group(self, type: EnumLessonType, _info):
        return type.value