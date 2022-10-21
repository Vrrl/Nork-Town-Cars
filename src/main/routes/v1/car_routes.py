from flask import Blueprint, request
from src.main.composer import (
    add_car_composer,
)
from src.main.adapter import flask_route_adapter

car_routes_bp = Blueprint("car_routes", __name__, url_prefix="/v1/cars")


@car_routes_bp.route("/", methods=["POST"])
def register_car():
    """register car route"""

    return flask_route_adapter(request=request, api_controller=add_car_composer())
