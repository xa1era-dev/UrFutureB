from typing import  Annotated, Literal, Union
from fastapi import APIRouter

from api.v1.endpoints import teacher
from .endpoints import course, profession, schedule, discipline, teacher
from core.schemas import ALL_SCHEMA_CLASSES

apiv1router = APIRouter(prefix="/api/v1")
apiv1router.include_router(course.courserouter)
apiv1router.include_router(profession.professionrouter)
apiv1router.include_router(schedule.schedulerouter)
apiv1router.include_router(discipline.disciplinerouter)
apiv1router.include_router(teacher.teacherrouter)

@apiv1router.get("/")
async def is_alive():
    """
    Запрос, чтобы проверить работу апи
    """
    return "1" #TODO: Сделать проверку работоспособности апи

@apiv1router.head("/") 
async def load_chemas(shemas: ALL_SCHEMA_CLASSES): # type: ignore
    return "all schemas refreshed"