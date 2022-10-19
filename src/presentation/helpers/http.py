from dataclasses import dataclass


@dataclass
class HttpRequest:
    """HttpRequest Representation Class"""

    header: dict = None
    body: dict = None
    query: dict = None


@dataclass
class HttpResponse:
    """HttpResponse Representation Class"""

    status_code: int
    body: dict = None
