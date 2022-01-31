from typing import Type, Tuple, Dict
from collections import namedtuple
import requests
from requests import Request
from src.errors import HttpRequestError
from src.data.interfaces.poloniex_api_consumer import PoloniexApiConsumerInterface

class PoloniexApiConsumer(PoloniexApiConsumerInterface):
    ''' Consume Poloniex api with http requests '''

    def __init__(self) -> None:
            self.get_currencies_response = namedtuple('GET_Currencies', 'status_code request response')

    def get_currencies(self) -> Tuple[Type[Request], Dict]:
        '''
            Request currencies information
            :param
            : return - Tuple with status_code, request, response attributes
        '''

        req = requests.Request(
            method='GET',
            url='https://poloniex.com/public?command=returnTicker'
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if ((status_code >= 200) and (status_code <= 299)):
                return self.get_currencies_response(
                    status_code = status_code, request = req, response = response.json()
                )
        else:
            raise HttpRequestError(
                message = response.json(), status_code = status_code
            )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        '''
            Prepare a session and send http request
            :param - req_prepared: Request Object with all params
            :response - Http response raw
        '''

        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
