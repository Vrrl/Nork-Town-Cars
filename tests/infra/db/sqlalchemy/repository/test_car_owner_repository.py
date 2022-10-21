from faker import Faker
from src.infra.db.sqlalchemy.repository import CarOwnerRepository
from src.domain.usecases import AddCarOwnerModel

faker = Faker()
car_owner_repository = CarOwnerRepository()


def test_add_car_owner_must_success():
    """Must successfully add a new valid car owner"""

    name = faker.name()

    new_car_owner = AddCarOwnerModel(name=name)

    response = car_owner_repository.add(new_car_owner)

    assert new_car_owner.name == response.name


def test_list_car_owner_must_success():
    """Must successfully list car owners"""

    limit = faker.random_int(1, 100)
    index = 0

    response = car_owner_repository.list(limit=limit, index=index)

    assert isinstance(response, list)
