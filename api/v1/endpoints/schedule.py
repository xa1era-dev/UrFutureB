from fastapi import APIRouter
from core.schemas import Course, LessonTime, Teacher, NotFoundApiError
from ..responses import *

schedulerouter = APIRouter(prefix="/schedule/build")

@schedulerouter.post("/", responses={**api_responses})
async def build_iot():
    raise NotFoundApiException("Not Implement")

@schedulerouter.get("/", responses={**api_responses})
async def get_iot():
    raise NotFoundApiException("Not Implement")

@schedulerouter.get("/courses", responses={**api_responses}, response_model=NotFoundApiError | list[Course])
async def get_iot_courses():
    raise NotFoundApiException("Not Implement")

@schedulerouter.put("/courses", responses={**api_responses})
async def set_iot_courses(courses: list[Course]):
    raise NotFoundApiException("Not Implement")

@schedulerouter.get("/time", responses={**api_responses}, response_model=NotFoundApiError | list[LessonTime])
async def get_iot_time():
    raise NotFoundApiException("Not Implement")

@schedulerouter.put("/time", responses={**api_responses})
async def set_iot_time(time: list[LessonTime]):
    raise NotFoundApiException("Not Implement")

@schedulerouter.get("/teachers", responses={**api_responses}, response_model=NotFoundApiError | list[LessonTime])
async def get_iot_teachers():
    raise NotFoundApiException("Not Implement")

@schedulerouter.put("/teachers", responses={**api_responses})
async def set_iot_teachers(teachers: list[Teacher]):
    raise NotFoundApiException("Not Implement")