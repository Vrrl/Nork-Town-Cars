from src.presentation.controllers import AddCarOwnerController
from src.application.services import AddCarOwnerService
from src.infra.db.sqlalchemy.repository import CarOwnerRepository


def add_car_owner_composer() -> AddCarOwnerController:
    """Composing Add Input Route
    :param - None
    :return - Object with Add Input Controller
    """

    repository = CarOwnerRepository()
    use_case = AddCarOwnerService(repository)
    add_car_owner_controller = AddCarOwnerController(use_case)

    return add_car_owner_controller
