from abc import ABC, abstractmethod

class CurrencyPriceRepositoryInterface(ABC):
    ''' Interface to Pet Repository '''

    @abstractmethod
    def insert_currency_price(self, currency_price) -> None:
        raise Exception("Method not implemented")
