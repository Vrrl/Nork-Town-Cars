from typing import Dict

from src.domain.usecases import AddCarUseCase, AddCarModel

from src.application.interfaces.repository import AddCarRepositoryInterface

from src.domain.models import Car


class AddCarService(AddCarUseCase):
    """Implementation of usercase: Add Car"""

    add_car_repository: AddCarRepositoryInterface

    def __init__(self, add_car_repository: AddCarRepositoryInterface):
        self.add_car_repository = add_car_repository

    def add(self, car: AddCarModel) -> Dict[bool, Car]:
        """Add Input use case
        :param - car: Model for add car usecase
        :return - Dictionary with informations of the process
        """

        response = None

        # TODO: doesnt have validation yet, make one
        validate_entry = True

        if validate_entry:
            response = self.add_car_repository.add(car)

        return {"Success": validate_entry, "Data": response}
