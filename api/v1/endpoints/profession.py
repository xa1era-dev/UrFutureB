from fastapi import APIRouter
from core.schemas import Profession, NotFoundApiError
from ..responses import *

professionrouter = APIRouter(prefix="/schedule/build")

@professionrouter.post("/")

@professionrouter.get("/all")
async def get_all_professions(response_model=list[Profession]):
    raise NotFoundApiException("Not Implement")

@professionrouter.get("/{pr_id}/courses", responses={**api_responses}, response_model=NotFoundApiError)
async def get_courses_by_profprofession(pr_id: int):
    raise NotFoundApiException("Not Implement")

@professionrouter.get("/{pr_id}", responses={**api_responses}, response_model=Profession | NotFoundApiError)
async def get_professions_by_id(pr_id: int):
    raise NotFoundApiException("dfsd")
