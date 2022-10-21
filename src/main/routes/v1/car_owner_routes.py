from flask import Blueprint, request
from src.main.composer import (
    add_car_owner_composer,
    list_car_owner_composer,
)
from src.main.adapter import flask_route_adapter

car_owner_routes_bp = Blueprint(
    "car_owner_routes", __name__, url_prefix="/v1/carowners"
)


@car_owner_routes_bp.route("/", methods=["POST"])
def register_car_owner():
    """register car owner route"""

    return flask_route_adapter(request=request, api_controller=add_car_owner_composer())


@car_owner_routes_bp.route("/", methods=["GET"])
def list_car_owners():
    """List car owners route"""

    return flask_route_adapter(
        request=request, api_controller=list_car_owner_composer()
    )
