from src.presentation.controllers import ListCarOwnerController
from src.application.services import ListCarOwnerService
from src.infra.db.sqlalchemy.repository import CarOwnerRepository


def list_car_owner_composer() -> ListCarOwnerController:
    """Composing Add Input Route
    :param - None
    :return - Object with List Input Controller
    """

    repository = CarOwnerRepository()
    use_case = ListCarOwnerService(repository)
    list_car_owner_controller = ListCarOwnerController(use_case)

    return list_car_owner_controller
