from abc import ABC, abstractmethod

class CurrencyRepositoryInterface(ABC):
    ''' Interface to Currency Repository '''

    @abstractmethod
    def insert_currency(self, currency) -> None:
        ''' Must implement '''
        raise Exception("Method not implemented")
