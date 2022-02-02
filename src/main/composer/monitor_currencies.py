from src.main.composer.get_currencies import get_currencies_composer
from src.main.tasks.monitor_currencies import CurrenciesMonitoring

def monitor_currencies_composer():
    ''' Composer to monitor currencies '''

    controller = get_currencies_composer()
    response = controller.handler()['data']
    currencies = [(currency_data['exchange_id'], currency_data['currency']) for currency_data in response]

    currencies_monitoring = CurrenciesMonitoring(currencies)
    currencies_monitoring.start_monitoring_currencies()
