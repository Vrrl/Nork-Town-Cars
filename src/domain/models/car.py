from dataclasses import dataclass
from enum import Enum


class CarColor(str, Enum):
    """Enum for Car Colors"""

    YELLOW = "yellow"
    BLUE = "blue"
    GRAY = "gray"


class CarModel(str, Enum):
    """Enum for Car Models"""

    HATCH = "hatch"
    SEDAN = "sedan"
    CONVERTIBLE = "convertible"


@dataclass
class Car:
    """Domain Model of Car"""

    id: str
    color: CarColor
    model: CarModel
    owner_id: str
