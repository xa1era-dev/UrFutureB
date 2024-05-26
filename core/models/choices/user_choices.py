from sqlalchemy import Column, Integer, String, ForeignKey, Table, UUID
from sqlalchemy.orm import relationship, Mapped
from ..base import Base
from ..user import User
from .half_period import HalfPeroid
from .lessons_time_choice import LessonTimeChoice
from .teacher_choice import TeacherChoice
import uuid


lessons_choices = Table('user_lessons_choices', Base.metadata,
    Column('user_choice_uuid', UUID(as_uuid=True), ForeignKey("user_choices.uuid")),
    Column('lesson_uuid', UUID(as_uuid=True), ForeignKey(LessonTimeChoice.uuid))
)

teachers_choices = Table("user_teachers_choices", Base.metadata,
    Column('user_choice_uuid', UUID(as_uuid=True), ForeignKey("user_choices.uuid")),
    Column("teacher_uuid", UUID(as_uuid=True), ForeignKey(TeacherChoice.uuid))
)

class Choices(Base):
    __tablename__ = "user_choices"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_uuid = Column(UUID, ForeignKey(User.uuid))
    half_uuid = Column(UUID, ForeignKey(HalfPeroid.uuid))
    lesson_times_uuids: Mapped[list[LessonTimeChoice]] = relationship(secondary=lessons_choices)
    teachers_uuids: Mapped[list[TeacherChoice]] = relationship(secondary=teachers_choices)