from src.data.interfaces import CurrencyRepositoryInterface
from src.domain.models import Currencies
from src.infra.config.db_config import get_connection

class CurrencyRepository(CurrencyRepositoryInterface):
    '''  '''

    @classmethod
    def insert_currency(cls, currency) -> Currencies:
        '''
        '''

        db, cursor = get_connection()

        try:
            sql = '''
                INSERT INTO currencies (exchange_id, currency)
                VALUES (%s, %s);
            '''
            cursor.executemany(sql, currency)

            db.commit()
        except:
            db.rollback()
