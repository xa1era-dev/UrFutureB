from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .course import course_tags


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Tag(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Tag: {self.name}"
    
    def __eq__(self, other):
        if not isinstance(other, Tag):
            raise TypeError("Нельзя сравнивать объекты других классов с объектами класса Tag")
        return self.id == other.id
    
    def __ne__(self, other):
        return not self == other
        
    def __hash__(self):
        return hash(self.id)

