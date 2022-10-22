from supertokens_python.recipe.session.framework.flask import verify_session

from flask import Blueprint, request

from src.main.composer import (
    list_sale_opportunity_composer,
)
from src.main.adapter import flask_route_adapter

sales_routes_bp = Blueprint("sales_routes", __name__, url_prefix="/v1/sales")


@sales_routes_bp.route("/opportunity", methods=["GET"])
@verify_session()
def list_sales_opportunity():
    """list sales opportunity route"""

    return flask_route_adapter(
        request=request, api_controller=list_sale_opportunity_composer()
    )
