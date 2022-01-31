from src.data.usecases.currencies_list_colector import CurrenciesListColector
from src.infra.poloniex_api_consumer import PoloniexApiConsumer
from src.presenters.controllers.currencies_list_colector import CurrenciesListColectorController

def get_currencies_composer():
    ''' Composer to get currencies '''

    infra = PoloniexApiConsumer()
    usecase = CurrenciesListColector(infra)
    controller = CurrenciesListColectorController(usecase)

    return controller
