from sqlalchemy import Column, Enum, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from .base import Base
from ..enums import ChangeType, ChangeStatus
from .course import Course
from .tag import Tag
from .discipline import Discipline  

class Change(Base):
    __tablename__ = 'change'

    id = Column(Integer, primary_key=True)
    change_type = Column(Enum(ChangeType), nullable=False) 
    new_value = Column(String, nullable=True)  
    description = Column(String, nullable=True) 
    
    entity_before_id = Column(Integer, nullable=True)
    entity_after_id = Column(Integer, nullable=True)
    
    course_id = Column(Integer, ForeignKey('course.id'), nullable=True)
    tag_id = Column(Integer, ForeignKey('tag.id'), nullable=True)
    discipline_id = Column(Integer, ForeignKey('discipline.id'), nullable=True)

    status = Column(Enum(ChangeStatus), nullable=False, default=ChangeStatus.created.value)  # Статус

    # Связи
    course = relationship('Course', foreign_keys=[course_id])
    tag = relationship('Tag', foreign_keys=[tag_id])
    discipline = relationship('Discipline', foreign_keys=[discipline_id])

    def __repr__(self):
        return (f"<Change(id={self.id}, change_type='{self.change_type}', "
                f"status='{self.status}', entity_before_id={self.entity_before_id}, "
                f"entity_after_id={self.entity_after_id})>")

    def __str__(self):
        return f"Change: {self.change_type} (Status: {self.status})"
