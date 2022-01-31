from abc import ABC, abstractmethod
from typing import Dict

class CurrenciesListColectorInterface(ABC):
    ''' Currencies Colector Interface '''

    @abstractmethod
    def list_currencies(self) -> Dict:
        ''' Must implement '''
        raise Exception('Must implement')