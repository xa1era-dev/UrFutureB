from sqlalchemy import Column, Enum, Integer, String, ForeignKey, Table
from core.models.base import Base


course_teachers = Table('course_teachers', Base.metadata,
    Column('teacher_id', Integer, ForeignKey('teacher.id')),
    Column('course_id', Integer, ForeignKey('course.id'))
)