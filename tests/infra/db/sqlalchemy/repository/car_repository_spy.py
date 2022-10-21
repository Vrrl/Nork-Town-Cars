from typing import Optional, List

from src.domain.models import Car

from src.domain.usecases import AddCarModel

from tests.domain.models import mock_car


class CarRepositorySpy:
    """Spy for Car Repository"""

    def __init__(self):
        self.add_car_params = {}
        self.list_car_params = {}

    def add(self, car: AddCarModel) -> Car:
        """Spy to all add attributes"""

        self.add_car_params["car"] = car

        return mock_car()

    def list(self, limit: Optional[int] = 100, index: Optional[int] = 0) -> List[Car]:
        """Spy to all list attributes"""

        self.list_car_params["limit"] = limit
        self.list_car_params["index"] = index

        return [mock_car() for i in range(0, limit)]
