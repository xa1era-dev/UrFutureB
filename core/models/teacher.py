from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # courses = relationship("Course", secondary="course_teachers")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Teacher: {self.name}"
