from abc import ABC, abstractmethod
from src.domain.models import Currencies

class CurrencyRepositoryInterface(ABC):
    ''' Interface to Pet Repository '''

    @abstractmethod
    def insert_currency(self, currency) -> Currencies:
        raise Exception("Method not implemented")
