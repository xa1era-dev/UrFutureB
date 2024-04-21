from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

course_tags = Table('course_tags', Base.metadata,
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

profession_tags = Table('profession_tags', Base.metadata,
    Column('profession_id', Integer, ForeignKey('professions.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=course_tags, back_populates="tags")
    professions = relationship("Profession", secondary=profession_tags, back_populates="tags")

    def __repr__(self):
        return f"<Tag(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Tag: {self.name}"
