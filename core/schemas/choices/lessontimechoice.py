from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
from pydantic import AliasChoices, AnyUrl, BaseModel, ConfigDict, Field, root_validator, validator
from typing import Annotated, Any, Literal
from ...enums import LessonChoiceState
from ..lesson_time import LessonTimeBase

class LessonTimeChoice(LessonTimeBase, BaseModel):
    state: LessonChoiceState