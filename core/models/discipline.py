from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from .base import Base
from .course import Course
from ..schemas import Discipline as DisciplineS
from ..schemas import Course as CourseS

discipline_courses = Table('discipline_courses', Base.metadata,
    Column('discipline_id', Integer, ForeignKey('discipline.id')),
    Column('course_id', Integer, ForeignKey('course.id'))
)

class Discipline(Base):
    __tablename__ = 'discipline'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    courses: Mapped[list["Course"]] = relationship("Course", secondary=discipline_courses, back_populates="disciplines")

    def __repr__(self):
        return f"<Discipline(id={self.id}, name='{self.name}', description='{self.description}')>"

    def __str__(self):
        return f"Discipline: {self.name}"
    
    def to_model(self) -> DisciplineS:
        return DisciplineS(**self.__dict__, courses=list(map(lambda c: CourseS(**c.__dict__), self.courses)))

