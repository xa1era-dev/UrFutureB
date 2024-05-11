from .ApiRouterCusotm import ApiRouterCustom
from fastapi.responses import JSONResponse
from core.schemas import Course, LessonType, NotFoundApiError, MissingArgumetsError, UnauthorizedApiError
from ..responses import *

courserouter = ApiRouterCustom(prefix="/course")

@courserouter.get("/all", response_model=list[Course])
async def get_all_courses():
    return [Course(**dict(name="Test", year=2027, course_type="traditional", description="Test course?", half=2, teachers=None, owner='fdg'))] # type: ignore

@courserouter.check_autorization()
@courserouter.get("/me/all", response_model=list[Course] | UnauthorizedApiError)
async def get_my_all_courses():
    return [Course(name="Test", year=2027, lessons_type=LessonType(type="traditional"), description="Test course?", half=2, teachers=None),
            Course(name="Test2", year=2024, lessons_type=LessonType(type="onlne"), description="Test course online?", half=2, teachers=None)]

@courserouter.get("/{course_id}", response_model=Course | NotFoundApiError | MissingArgumetsError | UnauthorizedApiError)
async def get_course_by_id(course_id: int):
    raise NotFoundApiException(f"Course with id:{course_id} doesn't not excists in database")
    raise NotImplementedException("get_course_by_id not implemented")
    #Делаем запрос к модели с данным id
    # return course_id
    return Course(name="Test", year=2024, lessons_type=LessonType(type="online"), desc="Test course?")
