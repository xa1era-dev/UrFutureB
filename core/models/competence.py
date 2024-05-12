from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from .base import Base

competence_tags = Table('competence_tags', Base.metadata,
    Column('competence_id', Integer, ForeignKey('competence.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Competence(Base):
    __tablename__ = 'competence'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique= True)
    description = Column(String)
    tags: Mapped[list["Tag"]] = relationship(secondary=competence_tags)
    
    def __repr__(self):
        return f"<Competence(id={self.id}, name='{self.name}', description='{self.description}')>"

    def __str__(self):
        return f"Competence: {self.name}"
