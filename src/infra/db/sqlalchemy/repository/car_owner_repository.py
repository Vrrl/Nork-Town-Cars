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


class CarOwnerRepository(
    AddCarOwnerRepositoryInterface, ListCarOwnersRepositoryInterface
):
    """Class to manage Car Owner Repository"""

    # pylint: disable=redefined-builtin
    def add(self, car_owner: AddCarOwnerModel) -> CarOwner:
        """
        Insert data in Car Owner entity
        :param - car_owner: Add Car Owner Model
        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_car_owner = CarOwnerEntity(name=car_owner.name)
                db_connection.session.add(new_car_owner)
                db_connection.session.commit()

                return CarOwner(
                    id=new_car_owner.id,
                    name=new_car_owner.name,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    def list(
        self, limit: Optional[int] = 100, index: Optional[int] = 0
    ) -> List[CarOwner]:
        """
        list data in Car Owner entity
        :param - limit: limit of entities
                - index: starting index offset
        :return - list of car owners
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = db_connection.session.query(CarOwnerEntity)

                # if name:
                #     query = query.filter_by(name=name)

                list_ = query.offset(index).limit(limit).all()

                return [
                    CarOwner(
                        id=car_owner.id,
                        name=car_owner.name,
                    )
                    for car_owner in list_
                ]
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
