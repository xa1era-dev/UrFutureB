from pydantic import BaseModel


class Teacher(BaseModel):
    name: str