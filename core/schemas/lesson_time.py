from pydantic import AliasChoices, BaseModel, ConfigDict, Field
from typing import Annotated
import datetime

class LessonTimeBase(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)
    
    day: Annotated[int, Field(ge=0, le=7)]
    start: datetime.datetime = Field(validation_alias=AliasChoices("start", "start_time"))
    end: Annotated[datetime.datetime, Field() ] = Field(validation_alias=AliasChoices("end", "end_time"))

class LessonTime(LessonTimeBase, BaseModel):
    week: Annotated[int, Field(ge=-1, le=10, default=-1)]