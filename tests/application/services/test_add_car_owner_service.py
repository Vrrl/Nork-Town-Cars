from string import digits
from faker import Faker

from src.domain.usecases import AddCarOwnerModel

from src.application.services import AddCarOwnerService

from tests.infra.db.sqlalchemy.repository import CarOwnerRepositorySpy


faker = Faker()


def test_add_car_owner_service_must_succeed():
    """Must successfully call add car owner service"""

    car_owner_repository = CarOwnerRepositorySpy()
    add_car_owner_service = AddCarOwnerService(car_owner_repository)

    new_car_owner = AddCarOwnerModel(name=faker.name())

    response = add_car_owner_service.add(new_car_owner)

    # Testing inputs
    assert car_owner_repository.add_car_owner_params["car_owner"] == new_car_owner

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_add_car_owner_service_must_fail():
    """Must fail to call add car owner service"""

    car_owner_repository = CarOwnerRepositorySpy()
    add_car_owner_service = AddCarOwnerService(car_owner_repository)

    new_car_owner = AddCarOwnerModel(name=faker.random_number(digits=2))

    response = add_car_owner_service.add(new_car_owner)

    # Testing inputs
    assert not car_owner_repository.add_car_owner_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
