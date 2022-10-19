from typing import Dict, List

from abc import ABC, abstractmethod


from src.domain.models import CarOwner


class ListCarOwnerUseCase(ABC):
    """Interface to List Car Owners use case"""

    # TODO: improve list filters
    @abstractmethod
    def add(self, car_owner: CarOwner) -> Dict[bool, List[CarOwner]]:
        """use case"""

        raise NotImplementedError()
