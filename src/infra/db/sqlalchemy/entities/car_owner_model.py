import uuid

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
)

from src.infra.db.sqlalchemy.base import Base


class CarOwner(Base):
    """Model class of Sqlachemy"""

    __tablename__ = "car_owners"

    id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)

    name = Column(String, nullable=False)

    cars = relationship("Cars", back_populates="car")
