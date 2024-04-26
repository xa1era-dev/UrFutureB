from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from .profession import Profession
from .course import Course
from .competence import Competence
from .lesson import Lesson
from .teacher import Teacher
from .tag import Tag

def create_session(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

