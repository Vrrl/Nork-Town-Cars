import random

from faker import Faker

from tests.application.services import AddCarServiceSpy

from src.domain.models import CarColor, CarModel
from src.domain.usecases import AddCarOwnerModel

from src.presentation.helpers import HttpRequest
from src.presentation.controllers import AddCarController

from src.infra.db.sqlalchemy.repository import CarOwnerRepository

faker = Faker()


def test_add_car_controller_must_succeed():
    """Must successfully call add car controller"""

    add_car_service = AddCarServiceSpy()
    add_car_controller = AddCarController(add_car_service)

    car_owner_repository = CarOwnerRepository()
    owner_name = faker.name()
    owner = car_owner_repository.add(AddCarOwnerModel(name=owner_name))

    body_attributes = {
        "color": random.choice(list(CarColor)).name,
        "model": random.choice(list(CarModel)).name,
        "owner_id": owner.id,
    }

    http_request = HttpRequest(body=body_attributes)

    response = add_car_controller.handle(http_request)

    # Testing input
    assert add_car_service.add_params["car"].color.name == body_attributes["color"].name
    assert add_car_service.add_params["car"].model.name == body_attributes["model"].name
    assert add_car_service.add_params["car"].owner_id == body_attributes["owner_id"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_add_car_owner_controller_must_fail_validation_blank_attribute():
    """Must fail to call add car owner controller"""

    add_car_service = AddCarServiceSpy()
    add_car_controller = AddCarController(add_car_service)

    body_attributes = {"color": "", "model": "", "owner_id": ""}

    http_request = HttpRequest(body=body_attributes)

    response = add_car_controller.handle(http_request)

    # Testing input
    assert not add_car_service.add_params

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_add_car_owner_controller_must_fail_validation_missing_attribute():
    """Must fail to call add car owner controller"""

    add_car_service = AddCarServiceSpy()
    add_car_controller = AddCarController(add_car_service)

    body_attributes = {
        "not_required_attribute": "random_value",
    }

    http_request = HttpRequest(body=body_attributes)

    response = add_car_controller.handle(http_request)

    # Testing input
    assert not add_car_service.add_params

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
