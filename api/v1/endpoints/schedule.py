from typing import Annotated, Literal
from fastapi import APIRouter
from core.schemas import Course, LessonTimeChoice, Teacher, NotImplementError, HalfPeroid
from core.models.database import create_session, DB_URL
from core.models.choices import user_choices 
from ..responses import *

schedulerouter = APIRouter(prefix="/schedule/build")

@schedulerouter.post("/")
async def build_iot():
    raise NotImplementedException("Not Implement")

@schedulerouter.get("/courses", response_model=list[Course] | NotImplementError)
async def get_iot_courses(descipline_id: int, year: int | None, half: Literal[1, 2] | None):
    if year and half:
        half_p = HalfPeroid(year=year, half=half)
    raise NotImplementedException("Not Implement")

@schedulerouter.put("/courses")
async def set_iot_courses(descipline_id: int, course_ids: list[int]):
    raise NotImplementedException("Not Implement")

@schedulerouter.get("/time", response_model=list[LessonTimeChoice] | NotImplementError )
async def get_iot_time(year: int | None, half: Literal[1, 2] | None):
    if year and half:
        half_p = HalfPeroid(year=year, half=half)
    raise NotImplementedException("Not Implement")

@schedulerouter.put("/time")
async def set_iot_time(lesson_time: list[LessonTimeChoice]):
    raise NotImplementedException("Not Implement")

@schedulerouter.get("/teachers", response_model=list[Teacher] | NotImplementError)
async def get_iot_teachers(descipline_id: int, year: int | None, half: Literal[1, 2] | None):
    if year and half:
        half_p = HalfPeroid(year=year, half=half)
    raise NotImplementedException("Not Implement")

@schedulerouter.put("/teachers")
async def set_iot_teachers(descipline_id: int, teacher_ids: list[int]):
    raise NotImplementedException("Not Implement")