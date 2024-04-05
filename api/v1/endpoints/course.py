from fastapi import APIRouter
from core.schemas.course import Course, LessonsType

route = APIRouter(prefix="/course")

@route.get("/{course_id}/")
async def get_course_by_id(course_id: int) -> Course:
    #Делаем запрос к модели с данным id
    # return course_id
    return Course(name="Test", year=2024, lessons_type=LessonsType(Type="online"), desc="Test course?")
