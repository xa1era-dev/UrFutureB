from pydantic import BaseModel, Field, model_validator
from enum import Enum
from typing import Literal

class LessonsType(BaseModel):
    Type: Literal["online", "traditional", "mixed"]
    owner: str = "УрФУ"
    platform: str | None = None #"ОК", "elearn", "ulear"... Только если online

    @model_validator(mode="after")
    def validate_platform(self):
        if self.Type != "online":
            self.platform = None
        return self

class Course(BaseModel):
    name: str
    year: int = Field(ge=2024)
    half: Literal[1, 2] = 1
    lessons_type: LessonsType
    img: str = "no_foto.img" #TODO: find src validation
    desc: str 