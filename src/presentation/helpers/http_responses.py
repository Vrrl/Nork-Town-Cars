from .http import HttpResponse
from . import status_code

# pylint: disable=invalid-name
def ok(body: dict) -> HttpResponse:
    """Http Response wrapper representing status code 200"""

    return HttpResponse(status_code=status_code.HTTP_200_OK, body=body)


def unprocessable(details: list) -> HttpResponse:
    """Http Response wrapper representing status code 422"""

    message = {
        "error": {
            "status": status_code.HTTP_422_UNPROCESSABLE_ENTITY,
            "title": "validation error",
            "detail": details,
        }
    }

    return HttpResponse(
        status_code=status_code.HTTP_422_UNPROCESSABLE_ENTITY, body=message
    )


def internal() -> HttpResponse:
    """Http Response wrapper representing status code 500"""

    message = {
        "error": {
            "status": status_code.HTTP_500_INTERNAL_SERVER_ERROR,
            "title": "Internal server error",
        }
    }

    return HttpResponse(
        status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR, body=message
    )
