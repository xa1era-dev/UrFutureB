from core.models.database import DB_URL, create_session
from .ApiRouterCusotm import ApiRouterCustom
from core.schemas import Discipline, LessonType, NotFoundApiError, NotImplementError, UnauthorizedApiError
from core.models import Course as CourseM
from ..responses import *

disciplinerouter = ApiRouterCustom(prefix="/discipline")

@disciplinerouter.get("/all", response_model=list[Discipline])
async def get_all_dicsiplines():
    raise NotImplementedException("get_my_all_dicsiplines")

@disciplinerouter.check_autorization()
@disciplinerouter.get("/me/all", response_model=list[Discipline] | UnauthorizedApiError | NotImplementError)
async def get_my_all_dicsiplines():
    raise NotImplementedException("get_my_all_dicsipline")

@disciplinerouter.get("/{dicsipline_id}", response_model=Discipline | NotFoundApiError | UnauthorizedApiError)
async def get_dicsipline_by_id(dicsipline_id: int):
    raise NotImplementedException("get_my_all_courses")
