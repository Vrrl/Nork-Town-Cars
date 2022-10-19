from typing import List, Optional

# from sqlalchemy.orm.exc import NoResultFound

from src.application.interfaces.repository import (
    AddCarOwnerRepositoryInterface,
    ListCarOwnersRepositoryInterface,
)

from src.domain.usecases import AddCarOwnerModel

from src.domain.models import CarOwner

from src.infra.db.sqlalchemy.config import DBConnectionHandler
from src.infra.db.sqlalchemy.entities import CarOwner as CarOwnerEntity


class CarOwnerReporitory(
    AddCarOwnerRepositoryInterface, ListCarOwnersRepositoryInterface
):
    """Class to manage Car Owner Repository"""

    # pylint: disable=redefined-builtin
    def add(self, car_owner: AddCarOwnerModel) -> CarOwner:
        """
        Insert data in PetsEntity entity
        :param - name: name of the pet
               - specie: Enum with species acepted
               - age: pet age
               - user_id: id of the owner (FK)
        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                ...

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
