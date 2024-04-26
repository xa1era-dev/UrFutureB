from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.schemas import Course, LessonsType, NotFoundApiError, MissingArgumetsError
from ..responses import *

courserouter = APIRouter(prefix="/course")

@courserouter.get("/all", response_model=list[Course], responses={**api_responses})
async def get_all_courses():
    return [Course(**dict(name="Test", year=2027, course_type="online", description="Test course?", half=2, teachers=None))] # type: ignore

@courserouter.get("/me/all", response_model=list[Course])
async def get_my_all_courses():
    #TODO: create check authorisation
    return [Course(name="Test", year=2027, lessons_type=LessonsType(course_type="online"), description="Test course?", half=2, teachers=None)]

@courserouter.get("/{course_id}", responses={**api_responses}, response_model=Course | NotFoundApiError)
async def get_course_by_id(course_id: int):
    raise NotFoundApiException("dfsd")
    #Делаем запрос к модели с данным id
    # return course_id
    return Course(name="Test", year=2024, lessons_type=LessonsType(Type="online"), desc="Test course?")
