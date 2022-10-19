from dataclasses import dataclass


@dataclass
class CarOwner:
    """Domain Model of Car owner"""

    id: str
    name: str
