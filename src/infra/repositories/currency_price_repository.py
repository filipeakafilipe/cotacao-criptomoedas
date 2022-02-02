from src.data.interfaces import CurrencyPriceRepositoryInterface
from src.infra.config.db_config import get_connection

class CurrencyPriceRepository(CurrencyPriceRepositoryInterface):
    '''  Currency Price quotation repository '''

    @classmethod
    def insert_currency_price(cls, currency_price) -> None:
        '''
            Insert quotation into database
        '''

        db, cursor = get_connection()

        try:
            sql = '''
                INSERT INTO currencies_prices (exchange_id, frequency, datetime, open, low, high, close)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            '''
            cursor.execute(sql, currency_price)

            db.commit()
        except:
            db.rollback()
