import os

from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    __conection_string: str
    session: Union[None, Session]

    def __init__(self):
        self.__conection_string = os.environ.get("DATABASE_CONNECTION_STRING")
        self.session = None

    def get_engine(self):
        """Return connection engine
        :param - None
        :return - engine connection to Database
        """

        engine = create_engine(self.__conection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__conection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
