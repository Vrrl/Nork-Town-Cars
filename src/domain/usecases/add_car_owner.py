from typing import Dict

from abc import ABC, abstractmethod

from dataclasses import dataclass

from src.domain.models import CarOwner


@dataclass
class AddCarOwnerModel:
    """Model for Add Car Owner Usecase"""

    name: str


class AddCarOwnerUseCase(ABC):
    """Interface to Add Car Owner use case"""

    @abstractmethod
    def add(self, car_owner: AddCarOwnerModel) -> Dict[bool, CarOwner]:
        """use case"""

        raise NotImplementedError()
