from sqlalchemy import Column, Integer, Enum, UUID
from sqlalchemy.orm import relationship, Mapped
from ...enums import LessonChoiceState
from ..base import Base
import uuid


class LessonTimeChoice(Base):
    __tablename__  = "lesson_time_choice"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    day = Column(Integer) #range(0, 7)
    time = Column(Integer) #range(0, 10)
    state = Column(Enum(LessonChoiceState), default=LessonChoiceState.NEUTRAL)