from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

course_tags = Table('course_tags', Base.metadata,
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    course_type = Column(String)
    created_by = Column(String)
    tags = relationship("Tag", secondary=course_tags, back_populates="courses")
    lessons = relationship("Lesson", back_populates="course")
    teachers = relationship("Teacher", secondary="course_teachers")

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', description='{self.description}')>"

    def __str__(self):
        return f"Course: {self.name}"

