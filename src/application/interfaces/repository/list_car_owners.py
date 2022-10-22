from abc import ABC, abstractmethod

from typing import Optional, List

from src.domain.models import CarOwner


class ListCarOwnersRepositoryInterface(ABC):
    """Interface to List Car Owners Repository"""

    @abstractmethod
    def list(
        self, has_cars: int, limit: Optional[int] = 100, index: Optional[int] = 0
    ) -> List[CarOwner]:
        """abstractmethod"""

        raise NotImplementedError()
