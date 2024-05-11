from sqlalchemy.orm.decl_api import DeclarativeMeta
from typing import Any, Iterable
from sqlalchemy.orm import sessionmaker, Session as S
from sqlalchemy.exc import InvalidRequestError, NoResultFound


class Session(S):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def insert(self, value: DeclarativeMeta | Iterable[DeclarativeMeta]):
        try:
            if isinstance(value, Iterable):
                self.add_all(value)
            else:
                self.add(value)
            self.commit()
        except:
            self.rollback()
        finally:
            self.close()

    def execute_query(self, query, expected_changes=None):
        try:
            result = self.execute(query)
            self.commit()
            if expected_changes is not None:
                if result.rowcount != expected_changes: # type: ignore
                    raise ValueError(f"Expected {expected_changes} changes, but {result.rowcount} changes were made") # type: ignore
        except (InvalidRequestError, NoResultFound) as e:
            print(f"Error executing query: {e}")
            self.rollback()
        else:
            if query.statement.is_selectable:
                return result.fetchall()
            else:
                return None
        