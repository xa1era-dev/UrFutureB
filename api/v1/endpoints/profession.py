from core.models.database import DB_URL, create_session
from .ApiRouterCusotm import ApiRouterCustom
from core.schemas import Profession, NotFoundApiError, NotImplementError
from core.models import Profession as ProfessionM
from ..responses import *

professionrouter = ApiRouterCustom(prefix="/professions")

# @professionrouter.post("/")

@professionrouter.get("/all", response_model=list[Profession])
async def get_all_professions():
    with create_session(DB_URL) as sess:
        return list(map(lambda c: Profession(**c.__dict__), sess.query(ProfessionM).all()))

@professionrouter.check_autorization()
@professionrouter.get("/me/all", response_model=list[Profession] | NotFoundApiError | NotImplementError)
async def get_courses_by_profprofession(pr_id: int):
    raise NotImplementedException("Not Implement")

@professionrouter.get("/{pr_id}", response_model=Profession | NotFoundApiError)
async def get_professions_by_id(pr_id: int):
    with create_session(DB_URL) as sess:
        raw_course = sess.query(ProfessionM).where(ProfessionM.id == pr_id).first()
        if (raw_course is None):
            raise NotFoundApiException(f"Profession with {pr_id} id doens't exists")
        return Profession(**raw_course.__dict__)
