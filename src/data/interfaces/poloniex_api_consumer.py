from abc import ABC, abstractmethod
from typing import Type, Tuple, Dict
from requests import Request

class PoloniexApiConsumerInterface(ABC):
    ''' Api Consumer Interface '''

    @abstractmethod
    def get_currencies(self) -> Tuple[Type[Request], Dict]:
        ''' Must implement '''
        raise Exception('Must implement')