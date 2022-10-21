from src.domain.models import Car, CarColor, CarModel

from src.domain.usecases import AddCarModel

from tests.domain.models import mock_car


class AddCarServiceSpy:
    """Spy for add Car service"""

    def __init__(self):
        self.add_params = {}

    def add(self, car: AddCarModel) -> Car:
        """Spy to all attributes"""

        self.add_params["car"] = car

        response = None

        validate_entry = (
            isinstance(car.owner_id, str)
            and car.owner_id is not None
            and isinstance(car.color, CarColor)
            and isinstance(car.model, CarModel)
        )

        if validate_entry:
            response = mock_car()

        return {"Success": validate_entry, "Data": response}
