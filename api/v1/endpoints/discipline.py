from core.models.database import DB_URL, create_session
from .ApiRouterCusotm import ApiRouterCustom
from core.schemas import Discipline, NotFoundApiError, NotImplementError, UnauthorizedApiError
from core.models import Discipline as DisciplineM
from ..responses import *

disciplinerouter = ApiRouterCustom(prefix="/discipline")

@disciplinerouter.get("/all", response_model=list[Discipline])
async def get_all_dicsiplines():
    with create_session(DB_URL) as sess:
        disciplines = sess.query(DisciplineM).all()
        res = list(map(lambda d: d.to_model(), disciplines))
        return res

@disciplinerouter.check_autorization()
@disciplinerouter.get("/me/all", response_model=list[Discipline] | UnauthorizedApiError | NotImplementError)
async def get_my_all_dicsiplines():
    raise NotImplementedException("get_my_all_dicsipline")

@disciplinerouter.get("/{dicsipline_id}", response_model=Discipline | NotFoundApiError | UnauthorizedApiError)
async def get_dicsipline_by_id(dicsipline_id: int):
    raise NotImplementedException("get_my_all_courses")
