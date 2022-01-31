from sqlalchemy import Column, Integer, String
from src.infra.config import Base

class Currencies(Base):
    ''' Currencies entity '''

    __tablename__ = 'currencies'

    id = Column(Integer, primary_key = True)
    exchange_id = Column(Integer, nullable = False, unique = True)
    currency = Column(String(20), nullable = False, unique = True)

    def __repr__(self):
            return f'Currency: Exchange_Id = {self.exchange_id}, Currency = {self.currency}'
