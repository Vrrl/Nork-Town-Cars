from typing import Dict, Optional

from abc import ABC, abstractmethod

from src.domain.models import Car


class ListCarsUseCase(ABC):
    """Interface to List Cars use case"""

    # TODO: improve list filters
    @abstractmethod
    def list(
        self, limit: Optional[int] = 100, start: Optional[int] = 0
    ) -> Dict[bool, Car]:
        """use case"""

        raise NotImplementedError()
