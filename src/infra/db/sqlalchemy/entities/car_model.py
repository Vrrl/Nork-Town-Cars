import uuid

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Enum,
)

from src.domain.models import CarColor, CarModel, CarOwner

from src.infra.db.sqlalchemy.base import Base


class Car(Base):
    """Model class of Sqlachemy"""

    __tablename__ = "cars"

    id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True)

    color = Column(Enum(CarColor))
    model = Column(Enum(CarModel))

    owner_id = Column(String, ForeignKey("car_owners.id"))
    owner = relationship("CarOwner", back_populates="cars")
