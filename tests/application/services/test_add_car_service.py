import random

from faker import Faker

from src.domain.models import CarColor, CarModel
from src.domain.usecases import AddCarModel, AddCarOwnerModel

from src.application.services import AddCarService

from src.infra.db.sqlalchemy.repository import CarOwnerRepository

from tests.infra.db.sqlalchemy.repository import CarRepositorySpy

faker = Faker()


def test_add_car_service_must_succeed():
    """Must successfully call add car owner service"""

    car_repository = CarRepositorySpy()
    add_car_service = AddCarService(car_repository)

    car_owner_repository = CarOwnerRepository()
    owner_name = faker.name()
    owner = car_owner_repository.add(AddCarOwnerModel(name=owner_name))

    color = random.choice(list(CarColor))
    model = random.choice(list(CarModel))
    new_car = AddCarModel(color=color, model=model, owner_id=owner.id)

    response = add_car_service.add(new_car)

    # Testing inputs
    assert car_repository.add_car_params["car"] == new_car

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_add_car_service_must_fail():
    """Must fail to call add car owner service"""

    car_repository = CarRepositorySpy()
    add_car_service = AddCarService(car_repository)

    owner_id = faker.name()
    color = faker.name()
    model = faker.name()

    new_car = AddCarModel(color=color, model=model, owner_id=owner_id)

    response = add_car_service.add(new_car)

    # Testing inputs
    assert not car_repository.add_car_params

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
