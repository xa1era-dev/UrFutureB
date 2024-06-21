from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from .base import Base
from ..schemas import Group as GroupS
from ..schemas import Lesson as LessonS
from .lesson import Lesson

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_ = Column(String)
    uuid_ = Column(String, unique=True)
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship("Course", back_populates="groups")
    lessons: Mapped[list["Lesson"]] = relationship("Lesson", back_populates="group")

    def __repr__(self):
        return f"<Group(id={self.id}, name='{self.name}', type_='{self.type_}', uuid_='{self.uuid_}')>"

    def __str__(self):
        return f"Group: {self.name}"

    def to_model(self) -> GroupS:
        return GroupS(**self.__dict__, lessons=list(map(lambda l: LessonS(**l.__dict__), self.lessons)))




