from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from ..enums import LessonRole


class BaseTeacher(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)
    
    id: int = 0
    name: str = ""
    second_name: str = ""
    third_name: str = ""
    img_src: str = ""
    kafedra: str = ""
    phone: PhoneNumber | None = None
    email: EmailStr | None = None
    
    
class Teacher(BaseTeacher):
    role: LessonRole = LessonRole.PRACTICIAN