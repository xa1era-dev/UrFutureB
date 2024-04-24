from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

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
