from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql://username:password@localhost/dbname'
engine = create_engine(DATABASE_URL)

Base = declarative_base()

lesson_tags = Table('lesson_tags', Base.metadata,
    Column('lesson_id', Integer, ForeignKey('lessons.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    lessons = relationship("Lesson", back_populates="course")


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Profession(Base):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Course", back_populates="lessons")
    tags = relationship("Tag", secondary=lesson_tags)


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    profession_id = Column(Integer, ForeignKey('professions.id'))
    profession = relationship("Profession")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()