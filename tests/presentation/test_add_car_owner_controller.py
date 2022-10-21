from faker import Faker
from tests.application.services import AddCarOwnerServiceSpy

from src.presentation.helpers import HttpRequest

from src.presentation.controllers import AddCarOwnerController

faker = Faker()


def test_add_car_owner_controller_must_succeed():
    """Must successfully call add car owner controller"""

    add_car_owner_service = AddCarOwnerServiceSpy()
    add_car_owner_controller = AddCarOwnerController(add_car_owner_service)

    body_attributes = {
        "name": faker.name(),
    }

    http_request = HttpRequest(body=body_attributes)

    response = add_car_owner_controller.handle(http_request)

    # Testing input
    assert add_car_owner_service.add_params["car_owner"].name == body_attributes["name"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_add_car_owner_controller_must_fail_validation_blank_attribute():
    """Must fail to call add car owner controller"""

    add_car_owner_service = AddCarOwnerServiceSpy()
    add_car_owner_controller = AddCarOwnerController(add_car_owner_service)

    body_attributes = {
        "name": "",
    }

    http_request = HttpRequest(body=body_attributes)

    response = add_car_owner_controller.handle(http_request)

    # Testing input
    assert not add_car_owner_service.add_params

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_add_car_owner_controller_must_fail_validation_missing_attribute():
    """Must fail to call add car owner controller"""

    add_car_owner_service = AddCarOwnerServiceSpy()
    add_car_owner_controller = AddCarOwnerController(add_car_owner_service)

    body_attributes = {
        "not_required_attribute": "random_value",
    }

    http_request = HttpRequest(body=body_attributes)

    response = add_car_owner_controller.handle(http_request)

    # Testing input
    assert not add_car_owner_service.add_params

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
