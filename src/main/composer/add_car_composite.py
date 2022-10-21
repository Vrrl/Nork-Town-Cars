from src.presentation.controllers import AddCarController
from src.application.services import AddCarService
from src.infra.db.sqlalchemy.repository import CarRepository


def add_car_composer() -> AddCarController:
    """Composing Add Car Route
    :param - None
    :return - Object with Add Car Controller
    """

    repository = CarRepository()
    use_case = AddCarService(repository)
    add_car_controller = AddCarController(use_case)

    return add_car_controller
