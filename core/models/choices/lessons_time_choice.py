from sqlalchemy import Column, Integer, Enum, UUID
from sqlalchemy.orm import relationship, Mapped
from ...enums import LessonChoiceState
from ..base import Base
import uuid


class LessonChoice(Base):
    __tablename__  = "lessonchoice"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    day = Column(Integer)
    time = Column(Integer)
    state = Column(Enum(LessonChoiceState), default=LessonChoiceState.NEUTRAL)