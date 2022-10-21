from faker import Faker
from tests.application.services import ListCarOwnerServiceSpy

from src.presentation.helpers import HttpRequest

from src.presentation.controllers import ListCarOwnerController

faker = Faker()


def test_list_car_owner_controller_must_fail():
    """Must successfully call list car owner controller"""

    list_car_owner_service = ListCarOwnerServiceSpy()
    list_car_owner_controller = ListCarOwnerController(list_car_owner_service)

    query_attributes = {
        "limit": faker.random_int(1, 100),
        "index": faker.random_int(),
    }

    http_request = HttpRequest(query=query_attributes)

    response = list_car_owner_controller.handle(http_request)

    # Testing input
    assert not list_car_owner_service.list_params

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_list_car_owner_controller_must_fail_validation_invalid_attributes():
    """Must fail to call list car owner controller"""

    list_car_owner_service = ListCarOwnerServiceSpy()
    list_car_owner_controller = ListCarOwnerController(list_car_owner_service)

    query_attributes = {
        "limit": faker.random_int(1000, 10000),
        "index": None,
    }

    http_request = HttpRequest(query=query_attributes)

    response = list_car_owner_controller.handle(http_request)

    # Testing input
    assert not list_car_owner_service.list_params

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_list_car_owner_controller_must_fail_validation_missing_attribute():
    """Must fail to call list car owner controller"""

    list_car_owner_service = ListCarOwnerServiceSpy()
    list_car_owner_controller = ListCarOwnerController(list_car_owner_service)

    query_attributes = {
        "not_required_attribute": "random_value",
    }

    http_request = HttpRequest(query=query_attributes)

    response = list_car_owner_controller.handle(http_request)

    # Testing input
    assert not list_car_owner_service.list_params

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
