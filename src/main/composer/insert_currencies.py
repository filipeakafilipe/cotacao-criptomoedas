from src.main.composer.get_currencies import get_currencies_composer
from src.infra.repositories.currency_repository import CurrencyRepository

def insert_currencies_composer():
    ''' Composer to insert filtred currencies '''

    controller = get_currencies_composer()
    response = controller.handler()['data']
    currencies = [(currency_data['exchange_id'], currency_data['currency']) for currency_data in response]
    currency_repository = CurrencyRepository()
    currency_repository.insert_currency(currencies)