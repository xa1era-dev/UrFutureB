from pydantic import BaseModel
from uuid import UUID
from core.enums.user_roles import UserRoles

class User(BaseModel):
    password: str
    username: str
    role: UserRoles = UserRoles.DEFAULT