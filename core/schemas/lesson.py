from typing import Annotated, Literal
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, validator

class LessonType(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)

    type: Annotated[str, Literal["online", "traditional", "mixed"], Field(validation_alias=AliasChoices("type", "course_type"))]
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


class LessonTime(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)
    
    week: Annotated[int, Field(ge=-1, le=10, default=-1)]
    day: Annotated[int, Field(ge=0, le=7)]
    time: Annotated[int, Field(ge=0, le=9), ] = Field(validation_alias="time")


class Lesson(BaseModel):
    class_: LessonTime
    type_: LessonType