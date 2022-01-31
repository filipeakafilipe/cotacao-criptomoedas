from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interfaces import CurrencyRepositoryInterface, currency_repository_interface
from src.domain.models import Currencies
from src.infra.config import DBConnectionHandler
from src.infra.entities import Currencies as CurrenciesModel

class CurrencyRepository(CurrencyRepositoryInterface):
    '''  '''

    @classmethod
    def insert_currency(cls, exchange_id: int, currency: str) -> Currencies:
        '''
        '''

        with DBConnectionHandler() as db_connection:
            try:
                new_currency = CurrenciesModel(exchange_id = exchange_id, currency = currency)
                db_connection.session.add(new_currency)
                db_connection.session.commit()

                return Currencies(
                    id = new_currency.id,
                    exchange_id = new_currency.exchange_id,
                    currency = new_currency.currency
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def get_currencies(cls) -> List[Currencies]:
        '''
        '''
        try:
            currencies = None

            with DBConnectionHandler() as db_connection:
                currencies = (
                    db_connection.session.query(CurrenciesModel)
                        .all()
                )

            return currencies
        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
