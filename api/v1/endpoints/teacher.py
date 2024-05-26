from core.models.database import DB_URL, create_session
from .ApiRouterCusotm import ApiRouterCustom
from core.schemas import Teacher, NotFoundApiError, NotImplementError, UnauthorizedApiError
from core.models import Teacher as TeacherM
from ..responses import *

teacherrouter = ApiRouterCustom(prefix="/teacher")

@teacherrouter.get("/all", response_model=list[Teacher])
async def get_all_courses():
    with create_session(DB_URL) as sess:
        return list(map(lambda c: Teacher(**c.__dict__), sess.query(TeacherM).all()))

@teacherrouter.check_autorization()
@teacherrouter.get("/me/all", response_model=list[Teacher] | UnauthorizedApiError | NotImplementError)
async def get_my_all_courses():
    raise NotImplementedException("get_my_all_courses")

@teacherrouter.get("/{teacher_id}", response_model=Teacher | NotFoundApiError | UnauthorizedApiError)
async def get_course_by_id(teacher_id: int):
    with create_session(DB_URL) as sess:
        raw_course = sess.query(TeacherM).where(TeacherM.id == teacher_id).first()
        if (raw_course is None):
            raise NotFoundApiException(f"Course with {teacher_id} id doens't exists")
        return Teacher(**raw_course.__dict__)
