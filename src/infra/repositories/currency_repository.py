from src.data.interfaces import CurrencyRepositoryInterface
from src.infra.config.db_config import get_connection

class CurrencyRepository(CurrencyRepositoryInterface):
    ''' Currencies repository '''

    @classmethod
    def insert_currency(cls, currency) -> None:
        '''
            Insert currency into repository
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
