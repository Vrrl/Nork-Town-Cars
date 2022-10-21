from typing import Dict, List, Optional

from src.domain.models import CarOwner

from tests.domain.models import mock_car_owner


class ListCarOwnerServiceSpy:
    """Spy for add Car Owner service"""

    def __init__(self):
        self.list_params = {}

    def list(
        self, limit: Optional[int] = 100, index: Optional[int] = 0
    ) -> Dict[bool, List[CarOwner]]:
        """Spy to all list attributes"""

        self.list_params["limit"] = limit
        self.list_params["index"] = index

        response = None

        validate_entry = isinstance(limit, int) and isinstance(index, int)

        if validate_entry:
            response = [mock_car_owner() for i in range(0, limit)]

        return {"Success": validate_entry, "Data": response}
