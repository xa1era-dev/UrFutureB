from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class Teacher(BaseModel):
    id: int = 0
    name: str
    second_name: str
    third_name: str
    img_src: str
    kafedra: str
    phone: PhoneNumber
    email: EmailStr