from abc import ABC, abstractmethod

from src.domain.models import CarOwner

from src.domain.usecases import AddCarOwnerModel


class AddCarOwnerRepositoryInterface(ABC):
    """Interface to Add Car Owner Repository"""

    @abstractmethod
    def add(self, car_owner: AddCarOwnerModel) -> CarOwner:
        """abstractmethod"""

        raise NotImplementedError()
