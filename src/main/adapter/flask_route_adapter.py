from typing import Type

from src.presentation.interfaces.controller import ControllerInterface
from src.presentation.helpers.http import HttpRequest, HttpResponse


def flask_adapter(request: any, api_controller: ControllerInterface) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    http_request = HttpRequest(
        header=request.headers, body=request.json, query=request.args.to_dict()
    )

    response = api_controller.route(http_request)

    return response
