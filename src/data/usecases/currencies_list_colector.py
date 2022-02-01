from typing import Dict, Type
from src.data.interfaces.poloniex_api_consumer import PoloniexApiConsumerInterface
from src.domain.usecases import CurrenciesListColectorInterface
from src.domain.models.valid_currencies import get_valid_currencies

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
    def __format_api_response(self, result: Dict) -> Dict:
        '''
            Format response from api request
            :params - result: Dict with all currencies information
            :returns - Dict with filtered currencies and only needed information
        '''
        valid_currencies = get_valid_currencies()

        result = [self.__format_valid_currencies(currency, result) for currency in valid_currencies]

        return result

    @classmethod
    def __format_valid_currencies(cls, currency, currencies):
        currency_data = currencies[currency]
        
        return {
            'exchange_id': currency_data['id'],
            'currency': currency,
            'last': currency_data['last']
        }       
