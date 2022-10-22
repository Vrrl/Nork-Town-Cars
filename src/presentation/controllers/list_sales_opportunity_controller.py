import logging

from validator import validate, Required, Blank, Not, Range

from src.presentation.helpers import http_responses
from src.presentation.helpers import HttpRequest, HttpResponse

from src.presentation.interfaces import ControllerInterface

from src.domain.usecases import ListSalesOpportunityUseCase


class ListSalesOpportunityController(ControllerInterface):
    """list Car Sales Controller"""

    list_sales_opportunity_use_case: ListSalesOpportunityUseCase

    def __init__(self, list_sales_opportunity_use_case: ListSalesOpportunityUseCase):
        self.list_sales_opportunity_use_case = list_sales_opportunity_use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Handle route to add car owner use case"""

        # Parsing
        parse_error = None
        try:
            http_request.query["page"] = int(http_request.query["page"])
            http_request.query["limit"] = int(http_request.query["limit"])
        except ValueError:
            parse_error = True
        except KeyError:
            parse_error = False

        if parse_error:
            return http_responses.unprocessable(details={"query": "Fail to parse"})

        # Validating
        query_rules = {
            "page": [Required, Not(Blank())],
            "limit": [Required, Not(Blank()), Range(1, 100)],
        }

        query_valid, query_errors = validate(query_rules, http_request.query)

        if not query_valid:
            return http_responses.unprocessable(details={"query": query_errors})

        # Handle
        try:
            response = self.list_sales_opportunity_use_case.list(
                index=http_request.query["page"], limit=http_request.query["limit"]
            )

            return http_responses.ok(body=response["Data"])

        # pylint: disable=broad-except
        except Exception as exc:
            logging.exception(exc)
            return http_responses.internal()
