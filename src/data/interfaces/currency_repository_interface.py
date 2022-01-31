from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Currencies

class CurrencyRepositoryInterface(ABC):
    ''' Interface to Pet Repository '''

    @abstractmethod
    def insert_currency(self, exchange_id: int, currency: str) -> Currencies:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_currencies(self) -> List[Currencies]:
        raise Exception("Method not implemented")
