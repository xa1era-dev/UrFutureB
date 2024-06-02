import uuid
from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from .teacher import BaseTeacher
from .lesson import Lesson


class Group(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)
    
    uuid_: uuid.UUID = uuid.uuid4()
    type_: str = "Практика"
    name: str = "" #АТ-11
    teachers: list[BaseTeacher] = []
    lessons: list[Lesson] = []