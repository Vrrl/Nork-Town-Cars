from abc import ABC, abstractmethod

from src.presentation.helpers import HttpRequest, HttpResponse


class ControllerInterface(ABC):
    """Interface for Controller presenter"""

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Handle the request"""
        raise NotImplementedError()
