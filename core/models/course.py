from sqlalchemy import Column, Enum, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from .tag import Tag
from .base import Base
from enums import Course_type



course_tags = Table('course_tags', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    Course_type = Column(Enum(Course_type))
    created_by = Column(String)
    tags: Mapped[list[Tag]] = relationship(secondary=course_tags)
    lessons = relationship("Lesson", back_populates="course")
    # teachers = relationship("Teacher", secondary="course_teachers")

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', description='{self.description}')>"

    def __str__(self):
        return f"Course: {self.name}"

