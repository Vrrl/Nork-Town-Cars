from typing import Dict

from src.domain.usecases import AddCarOwnerUseCase, AddCarOwnerModel

from src.application.interfaces.repository import (
    AddCarOwnerRepositoryInterface,
)

from src.domain.models import CarOwner


class AddCarOwnerService(AddCarOwnerUseCase):
    """Implementation of usercase: Add Car Owner"""

    add_car_owner_repository: AddCarOwnerRepositoryInterface

    def __init__(self, add_car_owner_repository: AddCarOwnerRepositoryInterface):
        self.add_car_owner_repository = add_car_owner_repository

    def add(self, car_owner: AddCarOwnerModel) -> Dict[bool, CarOwner]:
        """Add Input use case
        :param - car_owner: Model for add car owner usecase
        :return - Dictionary with informations of the process
        """

        response = None

        # Here we can also validate if already has car owner with this name
        # Name validation
        validate_entry = isinstance(car_owner.name, str) and car_owner.name is not None

        if validate_entry:
            response = self.add_car_owner_repository.add(car_owner)

        return {"Success": validate_entry, "Data": response}
