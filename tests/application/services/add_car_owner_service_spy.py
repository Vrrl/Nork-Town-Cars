from src.domain.models import CarOwner

from src.domain.usecases import AddCarOwnerModel

from tests.domain.models import mock_car_owner


class AddCarOwnerServiceSpy:
    """Spy for add Car Owner service"""

    def __init__(self):
        self.add_params = {}

    def add(self, car_owner: AddCarOwnerModel) -> CarOwner:
        """Spy to all attributes"""

        self.add_params["car_owner"] = car_owner

        response = None

        validate_entry = isinstance(car_owner.name, str) and car_owner.name is not None

        if validate_entry:
            response = mock_car_owner()

        return {"Success": validate_entry, "Data": response}
