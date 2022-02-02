from abc import ABC, abstractmethod

class CurrencyPriceRepositoryInterface(ABC):
    ''' Interface to Currency Price Repository '''

    @abstractmethod
    def insert_currency_price(self, currency_price) -> None:
        ''' Must implement '''
        raise Exception("Method not implemented")
