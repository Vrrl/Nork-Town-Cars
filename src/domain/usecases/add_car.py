from typing import Dict

from abc import ABC, abstractmethod

from dataclasses import dataclass

from src.domain.models import Car, CarColor, CarModel


@dataclass
class AddCarModel:
    """Model for Add Car Usecase"""

    color: CarColor
    model: CarModel
    owner_id: str


class AddCarUseCase(ABC):
    """Interface to Add Car use case"""

    @abstractmethod
    def add(self, car: Car) -> Dict[bool, Car]:
        """use case"""

        raise NotImplementedError()
