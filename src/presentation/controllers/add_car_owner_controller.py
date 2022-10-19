import logging

from validator import validate, Required, Blank, Not

from src.presentation.helpers import http_responses
from src.presentation.helpers import HttpRequest, HttpResponse

from src.presentation.interfaces import ControllerInterface

from src.domain.usecases import AddCarOwnerModel, AddCarOwnerUseCase


class AddCarOwnerController(ControllerInterface):
    """Add Car Owner Controller"""

    add_car_onwer_use_case: AddCarOwnerUseCase

    def __init__(self, add_car_onwer_use_case: AddCarOwnerUseCase):
        self.add_car_onwer_use_case = add_car_onwer_use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Handle route to add car owner use case"""

        body_rules = {"name": [Required, Not(Blank())]}

        body_valid, body_errors = validate(body_rules, http_request.body)

        if not body_valid:
            return http_responses.unprocessable(details={"body": body_errors})

        try:
            response = self.add_car_onwer_use_case.add(
                AddCarOwnerModel(http_request.body["name"])
            )

            return http_responses.ok(body=response["Data"].__dict__)

        # pylint: disable=broad-except
        except Exception as exc:
            logging.exception(exc)
            return http_responses.internal()
