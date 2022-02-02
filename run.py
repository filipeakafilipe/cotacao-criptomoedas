from src.main.composer.get_currencies import get_currencies_composer
from src.main.composer.monitor_currencies import monitor_currencies_composer
from src.infra.config.db_config import create_tables
from src.infra.repositories.currency_repository import CurrencyRepository

if __name__=="__main__":
    # response = None
    controller = get_currencies_composer()

    try:
        create_tables()
        response = controller.handler()['data']
        currencies = [(currency_data['exchange_id'], currency_data['currency']) for currency_data in response]
        currency_repository = CurrencyRepository()
        currency_repository.insert_currency(currencies)
        monitor_currencies_composer()
    except:
        pass
