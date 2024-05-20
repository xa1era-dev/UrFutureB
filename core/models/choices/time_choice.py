from sqlalchemy import Column, Integer, String, ForeignKey, Table, UUID
from sqlalchemy.orm import relationship, Mapped
from ..base import Base
import uuid

class TimeChoice(Base):
    __tablename__ = "time_choice"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    year = Column(Integer)
    half = Column(Integer)
    