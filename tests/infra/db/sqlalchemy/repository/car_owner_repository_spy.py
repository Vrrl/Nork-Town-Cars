from typing import Optional, List

from src.domain.models import CarOwner

from src.domain.usecases import AddCarOwnerModel

from tests.domain.models import mock_car_owner


class CarOwnerRepositorySpy:
    """Spy for Car Onwer Repository"""

    def __init__(self):
        self.add_car_owner_params = {}
        self.list_car_owner_params = {}

    def add(self, car_owner: AddCarOwnerModel) -> CarOwner:
        """Spy to all add attributes"""

        self.add_car_owner_params["car_owner"] = car_owner

        return mock_car_owner()

    def list(
        self, limit: Optional[int] = 100, index: Optional[int] = 0
    ) -> List[CarOwner]:
        """Spy to all list attributes"""

        self.list_car_owner_params["limit"] = limit
        self.list_car_owner_params["index"] = index

        return [mock_car_owner() for i in range(0, limit)]
