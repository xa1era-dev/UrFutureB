from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated

class LessonTimeBase(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)
    
    day: Annotated[int, Field(ge=0, le=7)]
    time: Annotated[int, Field(ge=0, le=9), ] = Field(validation_alias="time")

class LessonTime(LessonTimeBase, BaseModel):
    week: Annotated[int, Field(ge=-1, le=10, default=-1)]