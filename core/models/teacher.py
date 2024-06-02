from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped
from .base import Base
from .secondaries import course_teachers
from ..schemas import BaseTeacher as TeacherS

class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses: Mapped[list["Course"]] = relationship(secondary=course_teachers, back_populates="teachers") # type: ignore

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Teacher: {self.name}"
    
    def __int__(self) -> int:
        return self.id # type: ignore
    
    def to_model(self) -> TeacherS:
        return TeacherS(**self.__dict__)
