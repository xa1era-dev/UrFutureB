from sqlalchemy import Column, Integer, String, ForeignKey, Table, UUID
from sqlalchemy.orm import relationship, Mapped
from ..base import Base
from ..user import User
from .time_choice import TimeChoice
from .lessons_time_choice import LessonChoice
from .teacher_choice import TeacherChoice
import uuid

lessons_choices = Table('lessons_choices', Base.metadata,
    Column('user_uuid', UUID, ForeignKey(User.uuid)),
    Column('lesson_uuid', UUID, ForeignKey(LessonChoice.uuid))
)

teachers_choices = Table("teachers_choices", Base.metadata,
    Column('user_uuid', UUID, ForeignKey(User.uuid)),
    Column("teacher_uuid", UUID, ForeignKey(TeacherChoice.uuid))
)

class Choices(Base):
    __tablename__ = "user_choices"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_uuid = Column(UUID, ForeignKey(User.uuid))
    time_uuid = Column(UUID, ForeignKey(TimeChoice.uuid))
    lessons_uuids: Mapped[list[LessonChoice]] = relationship(secondary=lessons_choices)
    teachers_uuids: Mapped[list[TeacherChoice]] = relationship(secondary=teachers_choices)
    