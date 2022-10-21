from src.domain.models import CarOwner

from src.domain.usecases import AddCarOwnerModel

from tests.domain.models import mock_car_owner


class CarOwnerRepositorySpy:
    """Spy for Car Onwer Repository"""

    def __init__(self):
        self.add_car_owner_params = {}

    def add(self, car_owner: AddCarOwnerModel) -> CarOwner:
        """Spy to all attributes"""

        self.add_car_owner_params["car_owner"] = car_owner

        return mock_car_owner()
