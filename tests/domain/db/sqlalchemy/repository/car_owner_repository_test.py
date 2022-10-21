from faker import Faker
from src.infra.db.sqlalchemy.repository import CarOwnerRepository
from src.domain.usecases import AddCarOwnerModel

faker = Faker()
car_owner_repository = CarOwnerRepository()


def test_add_valid_car_owner_should_success():
    """Should successfully add a new valid car owner"""

    name = faker.name()

    new_car_owner = AddCarOwnerModel(name=name)

    response = car_owner_repository.add(new_car_owner)

    assert new_car_owner.name == response.name
