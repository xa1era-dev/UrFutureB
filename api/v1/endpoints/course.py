from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.schemas import Course, LessonsType, NotFoundApiError
from ..responses import *

route = APIRouter(prefix="/course")

@route.get("/all")
async def get_all_courses(response_model=list[Course]):
    return [Course(name="Test", year=2027, lessons_type=LessonsType(Type="online"), desc="Test course?", half=2)]

@route.get("/me/all")
async def get_my_all_courses(response_model=list[Course]):
    #TODO: create check authorisation
    return [Course(name="Test", year=2027, lessons_type=LessonsType(Type="online"), desc="Test course?", half=2)]

@route.get("/{course_id}", responses={**api_responses}, response_model=Course | NotFoundApiError)
async def get_course_by_id(course_id: int):
    raise NotFoundApiException("dfsd")
    #Делаем запрос к модели с данным id
    # return course_id
    return Course(name="Test", year=2024, lessons_type=LessonsType(Type="online"), desc="Test course?")
