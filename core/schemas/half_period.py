from pydantic import BaseModel, Field
from typing import Literal

class HalfPeroid(BaseModel):
    year: int = Field(ge=2024, default=2024)
    half: Literal[1, 2] = 1
    