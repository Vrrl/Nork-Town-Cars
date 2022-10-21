from flask import request as Request
from flask import jsonify

from src.presentation.interfaces.controller import ControllerInterface
from src.presentation.helpers.http import HttpRequest


def flask_route_adapter(request: Request, api_controller: ControllerInterface) -> any:
    """Adapter pattern to Flask
    :param - request: Flask Request
            - api_route: Composite Routes
    """

    header = request.headers
    body = request.get_json(silent=True)
    query = request.args.to_dict()

    if not header:
        header = {}

    if not body:
        body = {}

    if not query:
        query = {}

    http_request = HttpRequest(header=header, body=body, query=query)

    response = api_controller.handle(http_request)

    return jsonify(response.body), response.status_code
