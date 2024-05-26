from sqlalchemy import Column, Integer, String, ForeignKey, Table, UUID
from sqlalchemy.orm import relationship, Mapped
from ..base import Base
from ..teacher import Teacher
import uuid


class TeacherChoice(Base):
    __tablename__ = "teacher_choice"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = Column(Integer, ForeignKey(Teacher.id))
    place = Column(Integer)