from fastapi import APIRouter
from core.schemas import (Course, 
        LessonTime, Teacher,
        NotImplementError)
from ..responses import *

schedulerouter = APIRouter(prefix="/schedule/build")

@schedulerouter.post("/")
async def build_iot():
    raise NotImplementedException("Not Implement")

@schedulerouter.get("/")#TODO: schema for iot
async def get_iot():
    raise NotImplementedException("Not Implement")

@schedulerouter.get("/courses", response_model=NotImplementError | list[Course])
async def get_iot_courses():
    raise NotImplementedException("Not Implement")

@schedulerouter.put("/courses")
async def set_iot_courses(courses: list[Course]):
    raise NotImplementedException("Not Implement")

@schedulerouter.get("/time", response_model=NotImplementError | list[LessonTime])
async def get_iot_time():
    raise NotImplementedException("Not Implement")

@schedulerouter.put("/time")
async def set_iot_time(time: list[LessonTime]):
    raise NotImplementedException("Not Implement")

@schedulerouter.get("/teachers", response_model=NotImplementError | list[LessonTime])
async def get_iot_teachers():
    raise NotImplementedException("Not Implement")

@schedulerouter.put("/teachers")
async def set_iot_teachers(teachers: list[Teacher]):
    raise NotImplementedException("Not Implement")