from typing import Dict, List, Optional

from abc import ABC, abstractmethod


from src.domain.models import CarOwner


class ListCarOwnerUseCase(ABC):
    """Interface to List Car Owners use case"""

    # TODO: improve list filters
    @abstractmethod
    def list(
        self, limit: Optional[int] = 100, index: Optional[int] = 0
    ) -> Dict[bool, List[CarOwner]]:
        """use case"""

        raise NotImplementedError()
