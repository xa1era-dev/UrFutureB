from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

competence_tags = Table('competence_tags', Base.metadata,
    Column('competence_id', Integer, ForeignKey('competences.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Competence(Base):
    __tablename__ = 'competences'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    profession = relationship("Profession", back_populates="competences")
    tags = relationship("Tag_compenetce", secondary=competence_tags, back_populates="tags")
    def __repr__(self):
        return f"<Competence(id={self.id}, name='{self.name}', description='{self.description}')>"

    def __str__(self):
        return f"Competence: {self.name}"
