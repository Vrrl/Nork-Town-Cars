from flask import Blueprint, request
from src.main.composer import (
    add_car_owner_composer,
)
from src.main.adapter import flask_route_adapter

car_owner_routes_bp = Blueprint("car_owner_routes", __name__)


@car_owner_routes_bp.route("/carowners", methods=["POST"])
def register_car_owner():
    """register car owner route"""

    return flask_route_adapter(request=request, api_controller=add_car_owner_composer())
