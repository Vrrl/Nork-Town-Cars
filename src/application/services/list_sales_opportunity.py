from typing import Dict, List, Optional

from src.domain.usecases import ListSalesOpportunityUseCase

from src.application.interfaces.repository import ListCarOwnersRepositoryInterface

from src.domain.models import CarOwner


class ListSalesOportunityService(ListSalesOpportunityUseCase):
    """Implementation of usercase: list sales opportunity"""

    list_car_owners_repository: ListCarOwnersRepositoryInterface

    def __init__(self, list_car_owners_repository: ListCarOwnersRepositoryInterface):
        self.list_car_owners_repository = list_car_owners_repository

    def list(
        self, limit: Optional[int] = 100, start: Optional[int] = 0
    ) -> Dict[bool, List[CarOwner]]:
        """Add Input use case
        :param - limit(Optional): limit of objects.
                - start(Optional): index of search.
        :return - Dictionary with informations of the process
        """

        response = None

        # TODO: doesnt have validation yet, make one
        validate_entry = True

        if validate_entry:
            # TODO: Filter by car owners without cars
            response = self.list_car_owners_repository.list(limit, start)

        return {"Success": validate_entry, "Data": response}
