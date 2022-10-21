import logging

from validator import validate, Required, Blank, Not, In

from src.presentation.helpers import http_responses
from src.presentation.helpers import HttpRequest, HttpResponse

from src.presentation.interfaces import ControllerInterface

from src.domain.usecases import AddCarModel, AddCarUseCase
from src.domain.models import CarColor, CarModel


class AddCarController(ControllerInterface):
    """Add Car Controller"""

    add_car_use_case: AddCarUseCase

    def __init__(self, add_car_use_case: AddCarUseCase):
        self.add_car_use_case = add_car_use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Handle route to add car owner use case"""

        # Validating

        body_rules = {
            "color": [Required, Not(Blank()), In([color.name for color in CarColor])],
            "model": [Required, Not(Blank()), In([model.name for model in CarModel])],
            "owner_id": [Required, Not(Blank())],
        }

        body_valid, body_errors = validate(body_rules, http_request.body)

        if not body_valid:
            return http_responses.unprocessable(details={"body": body_errors})

        # Parsing
        http_request.body["color"] = CarColor[http_request.body["color"]]
        http_request.body["model"] = CarModel[http_request.body["model"]]

        try:
            response = self.add_car_use_case.add(
                AddCarModel(
                    color=http_request.body["color"],
                    model=http_request.body["model"],
                    owner_id=http_request.body["owner_id"],
                )
            )
            return http_responses.ok(body=response["Data"].__dict__)

        # pylint: disable=broad-except
        except Exception as exc:
            logging.exception(exc)
            return http_responses.internal()
