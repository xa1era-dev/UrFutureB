from typing import Annotated, Literal
from pydantic import BaseModel

class DisciplineChoice(BaseModel):
    courses: list[int]
    teachers: list[int]    

class Choices(BaseModel):
    time: Annotated[int, Literal[1, 2]]
    days: list[Literal[0, 1, 2, 3, 4, 5, 6]]
    disciplines: dict[int, DisciplineChoice]
