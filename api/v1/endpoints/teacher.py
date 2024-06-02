from core.models.database import DB_URL, create_session
from .ApiRouterCusotm import ApiRouterCustom
from core.schemas import BaseTeacher, NotFoundApiError, NotImplementError, UnauthorizedApiError
from core.models import Teacher as TeacherM
from ..responses import *

teacherrouter = ApiRouterCustom(prefix="/teacher")

@teacherrouter.get("/all", response_model=list[BaseTeacher])
async def get_all_teachers():
    with create_session(DB_URL) as sess:
        return list(map(lambda c: BaseTeacher(**c.__dict__), sess.query(TeacherM).all()))

@teacherrouter.check_autorization()
@teacherrouter.get("/me/all", response_model=list[BaseTeacher] | UnauthorizedApiError | NotImplementError)
async def get_my_all_teachers():
    raise NotImplementedException("get_my_all_courses")

@teacherrouter.get("/{teacher_id}", response_model=BaseTeacher | NotFoundApiError | UnauthorizedApiError)
async def get_teacher_by_id(teacher_id: int):
    with create_session(DB_URL) as sess:
        raw_course = sess.query(TeacherM).where(TeacherM.id == teacher_id).first()
        if (raw_course is None):
            raise NotFoundApiException(f"Course with {teacher_id} id doens't exists")
        return BaseTeacher(**raw_course.__dict__)
