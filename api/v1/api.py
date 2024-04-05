from fastapi import APIRouter
from .endpoints import course

route = APIRouter(prefix="/api/v1")
route.include_router(course.route)

@route.get("/")
async def is_alive():
    """
    Запрос, чтобы проверить работу апи
    """
    return "1" #TODO: Сделать проверку работоспособности апи