from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
from pydantic import AliasChoices, AnyUrl, BaseModel, ConfigDict, Field, root_validator, validator
from typing import Annotated, Any, Literal
from .course import Course

class Discipline(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True)

    id: int = 0
    name: str = ""
    description: str | None = ""
    courses: list[Course | int] = []

