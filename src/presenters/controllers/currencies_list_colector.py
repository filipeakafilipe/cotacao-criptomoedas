from src.domain.usecases.currencies_list_colector import CurrenciesListColectorInterface
from src.presenters.interfaces.controllers import ControllersInterface

class CurrenciesListColectorController(ControllersInterface):
    ''' Controller to list currencies '''

    def __init__(self, currencies_list_colector: CurrenciesListColectorInterface) -> None:
        self.__use_case = currencies_list_colector

    def handler(self):
        ''' Handler to list currencies '''

        currencies_list = self.__use_case.list_currencies()
        http_response = { 'status_code': 200, 'data': currencies_list }

        return http_response
