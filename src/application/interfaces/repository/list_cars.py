from abc import ABC, abstractmethod

from typing import Optional, List

from src.domain.models import Car


class ListCarsRepositoryInterface(ABC):
    """Interface to List Cars Repository"""

    @abstractmethod
    def list(self, limit: Optional[int] = 100, start: Optional[int] = 0) -> List[Car]:
        """abstractmethod"""

        raise NotImplementedError()
