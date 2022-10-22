from supertokens_python.recipe.session.framework.flask import verify_session

from flask import Blueprint, request

from src.main.composer import (
    add_car_composer,
)
from src.main.adapter import flask_route_adapter

car_routes_bp = Blueprint("car_routes", __name__, url_prefix="/v1/cars")


@car_routes_bp.route("/", methods=["POST"])
@verify_session()
def register_car():
    """register car route"""

    return flask_route_adapter(request=request, api_controller=add_car_composer())


@car_routes_bp.route("/", methods=["GET"])
def list_car():
    """list car route"""

    return
