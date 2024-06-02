from pydantic import BaseModel

class WorkData(BaseModel):
    min_salary: int
    max_salary: int
    count_vacancy: int 

class Profession(BaseModel):
    id: int
    name: str
    description: str | None = None
    img_src: str | None = None
    data: WorkData | None = None