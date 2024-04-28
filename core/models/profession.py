from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

profession_tags = Table('profession_tags', Base.metadata,
    Column('profession_id', Integer, ForeignKey('professions.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)
class Profession(Base):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = relationship("Tag", back_populates="professions")
    competences = relationship("Competence", back_populates="profession")

    def __repr__(self):
        return f"<Profession(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Profession: {self.name}"
