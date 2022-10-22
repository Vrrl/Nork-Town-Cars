from src.presentation.controllers import ListSalesOpportunityController
from src.application.services import ListSalesOportunityService
from src.infra.db.sqlalchemy.repository import CarOwnerRepository


def list_sale_opportunity_composer() -> ListSalesOpportunityController:
    """Composing list sales opportunity
    :param - None
    :return - Object with List sales opportunity Controller
    """

    repository = CarOwnerRepository()
    use_case = ListSalesOportunityService(repository)
    list_sales_opportunity_controller = ListSalesOpportunityController(use_case)

    return list_sales_opportunity_controller
