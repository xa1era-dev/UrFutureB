from sqlalchemy import Column, Enum, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from .base import Base
from .tag import Tag
from ..enums import Course_type
from ..schemas import Course as CourseS
from .teacher import Teacher
from .lesson import Lesson
from .group import Group
from .secondaries import course_teachers
from .discipline import Discipline, discipline_courses

course_tags = Table('course_tags', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    course_type = Column(Enum(Course_type), server_default=Course_type.traditional.value)
    year = Column(Integer)
    created_by = Column(String)
    tags: Mapped[list[Tag]] = relationship("Tag", secondary=course_tags, back_populates="courses")
    groups: Mapped[list["Group"]] = relationship("Group", back_populates="course")
    teachers: Mapped[list[Teacher]] = relationship(secondary=course_teachers)
    disciplines: Mapped[list["Discipline"]] = relationship("Discipline", secondary=discipline_courses, back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', description='{self.description}')>"

    def __str__(self):
        return f"Course: {self.name}"
    
    def __int__(self):
        return self.id
    
    def to_model(self) -> CourseS:
        return CourseS(**self.__dict__, teachers=list(map(lambda t: t.to_model(), self.teachers)), groups=list(map(lambda g: g.to_model(), self.groups)))



