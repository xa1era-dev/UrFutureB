from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
from pydantic import AliasChoices, AnyUrl, BaseModel, ConfigDict, Field, root_validator, validator
from typing import Annotated, Any, Literal
from .lesson import Lesson
from .half_period import HalfPeroid
from .course import Course

class IOT(BaseModel):
    half_period: HalfPeroid
    courses_ids: list[int]
    lessons: list[Lesson]