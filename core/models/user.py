from sqlalchemy import Column, Enum, Integer, String, ForeignKey, Table, UUID
from sqlalchemy.orm import relationship, Mapped
from .base import Base
from ..enums import UserRoles
import uuid

class User(Base):
    __tablename__ = "user"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True)
    password = Column(String)
    username = Column(String)
    role = Column(Enum(UserRoles), default=UserRoles.DEFAULT)
    image_src = Column(String)
