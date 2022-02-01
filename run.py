from venv import create
from src.main.composer.get_currencies import get_currencies_composer
from src.infra.config.db_config import create_tables
from src.infra.repositories.currency_repository import CurrencyRepository

if __name__=="__main__":
    # create_tables()
    # currency = (1, 'TEST_CURRENCY')
    # currency_repository = CurrencyRepository()
    # currency_repository.insert_currency(currency)

    response = None
    controller = get_currencies_composer()

    try:
        # create_tables()
        response = controller.handler()['data']
        currencies = [(currency_data['exchange_id'], currency_data['currency']) for currency_data in response]
        currency_repository = CurrencyRepository()
        currency_repository.insert_currency(currencies)
    except:
        pass

    print(response)
