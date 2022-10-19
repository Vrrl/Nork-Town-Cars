from typing import Dict, List, Optional

from src.domain.usecases import ListCarsUseCase

from src.application.interfaces.repository import ListCarsRepositoryInterface

from src.domain.models import Car


class ListCarsService(ListCarsUseCase):
    """Implementation of usercase: list Cars"""

    list_cars_repository: ListCarsRepositoryInterface

    def __init__(self, list_cars_repository: ListCarsRepositoryInterface):
        self.list_cars_repository = list_cars_repository

    def list(
        self, limit: Optional[int] = 100, start: Optional[int] = 0
    ) -> Dict[bool, List[Car]]:
        """Add Input use case
        :param - limit(Optional): limit of objects.
                - start(Optional): index of search.
        :return - Dictionary with informations of the process
        """

        response = None

        # TODO: doesnt have validation yet, make one
        validate_entry = True

        if validate_entry:
            response = self.list_cars_repository.list(limit, start)

        return {"Success": validate_entry, "Data": response}
