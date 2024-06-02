from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from ..schemas import Lesson as LessonS

class Lesson(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    course_id = Column(Integer, ForeignKey('course.id'))
    # course = relationship("Course", back_populates="lessons")

    def __repr__(self):
        return f"<Lesson(id={self.id}, title='{self.title}', course_id={self.course_id})>"

    def __str__(self):
        return f"Lesson: {self.title}"

    def to_model(self) -> LessonS:
        return LessonS(**self.__dict__)
