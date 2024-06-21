from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from ..schemas import Lesson as LessonS

class Lesson(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    group_id = Column(Integer, ForeignKey('group.id'))  # Внешний ключ для связи с группой
    group = relationship("Group", back_populates="lessons")  # Связь с группой

    def __repr__(self):
        return f"<Lesson(id={self.id}, title='{self.title}', group_id={self.group_id})>"

    def __str__(self):
        return f"Lesson: {self.title}"

    def to_model(self) -> LessonS:
        return LessonS(**self.__dict__)


