from dataclasses import dataclass
from pyexpat import model

from enum import Enum


class CarColor(Enum):
    YELLOW = "yellow"
    BLUE = "blue"
    GRAY = "gray"


class CarModel(Enum):
    HATCH = "hatch"
    SEDAN = "sedan"
    CONVERTIBLE = "convertible"


@dataclass
class Car:
    id: str
    name: str
    color: CarColor
    model: CarModel
    owner_id: str
