from typing import List, Optional

from sqlalchemy import func

# from sqlalchemy.orm.exc import NoResultFound

from src.application.interfaces.repository import (
    AddCarOwnerRepositoryInterface,
    ListCarOwnersRepositoryInterface,
)

from src.domain.usecases import AddCarOwnerModel

from src.domain.models import CarOwner

from src.infra.db.sqlalchemy.config import DBConnectionHandler
from src.infra.db.sqlalchemy.entities import CarOwner as CarOwnerEntity
from src.infra.db.sqlalchemy.entities import Car as CarEntity


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
        self,
        has_cars: bool = True,
        limit: Optional[int] = 100,
        index: Optional[int] = 0,
    ) -> List[CarOwner]:
        """
        list data in Car Owner entity
        :param - max_cars: maximun cars of the car owner
                - limit: limit of entities
                - index: starting index offset
        :return - list of car owners
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = db_connection.session.query(CarOwnerEntity)

                # TODO: IMPORTANT LOGIC REFAC
                # as the project requirements is to filter by car owner without cars,
                # the choise made was to make a filter by number of cars but i got trouble by making with `having`
                # sqlalchemy statement idkw and i ended up creating just a filter for car owner that doesnt have car that works.
                # the current project purpose doesnt require this refactor as it works as it need but
                # it will be better with propely logic refactor
                if not has_cars:
                    # pylint: disable=singleton-comparison
                    query = query.filter(CarOwnerEntity.cars == None)

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
