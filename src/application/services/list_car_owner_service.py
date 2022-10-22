from typing import Dict, List, Optional

from src.domain.usecases import ListCarOwnerUseCase

from src.application.interfaces.repository import ListCarOwnersRepositoryInterface

from src.domain.models import CarOwner


class ListCarOwnerService(ListCarOwnerUseCase):
    """Implementation of usercase: list Car onwer"""

    list_car_owners_repository: ListCarOwnersRepositoryInterface

    def __init__(self, list_car_owners_repository: ListCarOwnersRepositoryInterface):
        self.list_car_owners_repository = list_car_owners_repository

    def list(
        self, limit: Optional[int] = 100, index: Optional[int] = 0
    ) -> Dict[bool, List[CarOwner]]:
        """Add Input use case
        :param - limit(Optional): limit of objects.
                - start(Optional): index of search.
        :return - Dictionary with informations of the process
        """

        response = None

        validate_entry = isinstance(limit, int) and isinstance(index, int)

        if validate_entry:
            response = self.list_car_owners_repository.list(limit=limit, index=index)

        return {"Success": validate_entry, "Data": response}
