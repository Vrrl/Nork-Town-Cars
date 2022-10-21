from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime


class BaseClass(object):
    """Base class for declarative base"""

    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


Base = declarative_base(cls=BaseClass)


def create_database(engine) -> None:
    """Create database tables if not exist"""
    Base.metadata.create_all(bind=engine)
