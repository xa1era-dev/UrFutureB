from contextlib import contextmanager
import re
from typing import overload
from sqlalchemy import MetaData, create_engine
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
                    {env("POSTGRES_PASSWORD", "postgres")}@
                    {env("POSTGRES_SERVER", "localhost")}:
                    {env("POSTGRES_PORT", "5432")}/
                    {env("POSTGRES_DB", 'postgres')}""")

@contextmanager
def create_session(DB_URL: str):
    engine = create_engine(DB_URL)
    session = sessionmaker(class_=Session, bind=engine, expire_on_commit=False)()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

