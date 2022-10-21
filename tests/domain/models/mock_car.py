import random

from faker import Faker

from src.domain.models import Car, CarColor, CarModel

faker = Faker()


def mock_car() -> Car:
    """Mocking Car"""

    return Car(
        id=faker.uuid4(),
        color=random.choice(list(CarColor)),
        model=random.choice(list(CarModel)),
        owner_id=faker.uuid4(),
    )
