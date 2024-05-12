from core.models.database import DB_URL, create_session
from .ApiRouterCusotm import ApiRouterCustom
from core.schemas import Course, LessonType, NotFoundApiError, NotImplementError, UnauthorizedApiError
from core.models import Course as CourseM
from ..responses import *

courserouter = ApiRouterCustom(prefix="/course")

@courserouter.get("/all", response_model=list[Course])
async def get_all_courses():
    with create_session(DB_URL) as sess:
        return list(map(lambda c: Course(**c.__dict__), sess.query(CourseM).all()))

@courserouter.check_autorization()
@courserouter.get("/me/all", response_model=list[Course] | UnauthorizedApiError | NotImplementError)
async def get_my_all_courses():
    raise NotImplementedException("get_my_all_courses")
    return [Course(name="Test", year=2027, lessons_type=LessonType(type="traditional"), description="Test course?", half=2, teachers=[]),
            Course(name="Test2", year=2024, lessons_type=LessonType(type="onlne"), description="Test course online?", half=2, teachers=[])]

@courserouter.get("/{course_id}", response_model=Course | NotFoundApiError | UnauthorizedApiError)
async def get_course_by_id(course_id: int):
    with create_session(DB_URL) as sess:
        raw_course = sess.query(CourseM).where(CourseM.id == course_id).first()
        if (raw_course is None):
            raise NotFoundApiException(f"Course with {course_id} id doens't exists")
        return Course(**raw_course.__dict__)
