from faker import Faker

from src.application.services import ListCarOwnerService

from tests.infra.db.sqlalchemy.repository import CarOwnerRepositorySpy


faker = Faker()


def test_list_car_owner_service_must_succeed():
    """Must successfully call list car owner service"""

    car_owner_repository = CarOwnerRepositorySpy()
    add_car_owner_service = ListCarOwnerService(car_owner_repository)

    limit = faker.random_int(1, 100)
    index = faker.random_int()

    response = add_car_owner_service.list(limit=limit, index=index)

    # Testing inputs
    assert car_owner_repository.list_car_owner_params["limit"] == limit
    assert car_owner_repository.list_car_owner_params["index"] == index

    # Testing outputs
    assert response["Success"] is True
    assert isinstance(response["Data"], list)


def test_list_car_owner_service_must_fail():
    """Must fail to call list car owner service"""

    car_owner_repository = CarOwnerRepositorySpy()
    add_car_owner_service = ListCarOwnerService(car_owner_repository)

    limit = faker.random_int(300, 1000)
    index = None

    response = add_car_owner_service.list(limit=limit, index=index)

    # Testing inputs
    assert not car_owner_repository.list_car_owner_params

    # Testing outputs
    assert response["Success"] is False
