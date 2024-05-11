import pathlib
import re
from typing import overload
from sqlalchemy import create_engine
from .base import Base
from .profession import Profession
from .course import Course
from .competence import Competence
from .lesson import Lesson
from .teacher import Teacher
from .tag import Tag
from ._session import Session
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv(r"c:\Users\IEBul\OneDrive\UrFuture\envvars\db.env")



def env(name: str, default: str | None = None) -> str | None:
    return os.environ.get(name, default)

DB_URL = re.sub("(\n|\s)+", "",  # type: ignore
                f"""postgresql://{env("POSTGRES_USER", "postgres")}:
                    {env("POSTGRES_PSW", "postgres")}@
                    {env("POSTGRES_SERVER", "localhost")}:
                    {env("POSTGRES_PORT", "5433")}/
                    {env("POSTGRES_DB", 'postgres')}""")

def create_session(DB_URL: str) -> Session:
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    session = sessionmaker(class_=Session, bind=engine, )
    return session()

