from pydantic import BaseModel

class WorkData(BaseModel):
    min_salary: int
    max_salary: int
    count_vacancy: int 

class Profession(BaseModel):
    id: int
    name: str
    description: str
    img_src: str
    data: WorkData