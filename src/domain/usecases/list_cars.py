from typing import Dict

from abc import ABC, abstractmethod

from src.domain.models import Car


class ListCarsUseCase(ABC):
    """Interface to List Cars use case"""

    # TODO: improve list filters
    @abstractmethod
    def list(self, car: Car) -> Dict[bool, Car]:
        """use case"""

        raise NotImplementedError()
