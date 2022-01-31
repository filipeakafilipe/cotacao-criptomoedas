from typing import Dict, Type
from src.data.interfaces.poloniex_api_consumer import PoloniexApiConsumerInterface
from src.domain.usecases import CurrenciesListColectorInterface

class CurrenciesListColector(CurrenciesListColectorInterface):
    ''' CurrenciesListColector '''

    def __init__(self, api_consumer: Type[PoloniexApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list_currencies(self) -> Dict:
        '''
            List currencies informations
            :params
            :returns - Dict with all currencies last informations
        '''

        api_response = self.__api_consumer.get_currencies()
        currencies_filtered = self.__format_api_response(api_response.response)
        return currencies_filtered

    @classmethod
    def __format_api_response(cls, result: Dict) -> Dict:
        '''
            Format response from api request
            :params - result: Dict with all currencies information
            :returns - Dict with filtered currencies and only needed information
        '''

        return result