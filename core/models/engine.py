from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError, NoResultFound

engine = create_engine("postgresql://postgres:postgres@localhost/postgres")
Session = sessionmaker(bind=engine)

Base = declarative_base()

class YourTable(Base):
    __tablename__ = 'your_table'
    id = Column(Integer, primary_key=True)

def insert(value):
    session = Session()
    try:
        session.add(value)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def execute_query(query, expected_changes=None):
    session = Session()
    try:
        result = session.execute(query)
        session.commit()
        if expected_changes is not None:
            if result.rowcount != expected_changes:
                raise ValueError(f"Expected {expected_changes} changes, but {result.rowcount} changes were made")
    except (InvalidRequestError, NoResultFound) as e:
        print(f"Error executing query: {e}")
        session.rollback()
        raise
    else:
        if query.statement.is_selectable:
            return result.fetchall()
        else:
            return None






