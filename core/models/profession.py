from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from .tag import Tag
from .base import Base

profession_tags = Table('profession_tags', Base.metadata,
    Column('profession_id', Integer, ForeignKey('profession.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)
class Profession(Base):
    __tablename__ = 'profession'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    tags: Mapped[list[Tag]] = relationship(secondary=profession_tags)

    def __repr__(self):
        return f"<Profession(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Profession: {self.name}"
