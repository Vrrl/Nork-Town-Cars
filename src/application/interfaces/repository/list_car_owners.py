from abc import ABC, abstractmethod

from typing import Optional, List

from src.domain.models import CarOwner


class ListCarOwnersRepositoryInterface(ABC):
    """Interface to List Car Owners Repository"""

    @abstractmethod
    def list(
        self, limit: Optional[int] = 100, start: Optional[int] = 0
    ) -> List[CarOwner]:
        """abstractmethod"""

        raise NotImplementedError()
