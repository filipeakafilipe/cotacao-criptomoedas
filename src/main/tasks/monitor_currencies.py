from src.infra.repositories.currency_price_repository import CurrencyPriceRepository
from src.main.composer.get_currencies import get_currencies_composer
from src.domain.models.frequencies import get_frequencies
import schedule
from datetime import datetime

class CurrenciesMonitoring:
    def __init__(self, currencies) -> None:
        self.frequencies = get_frequencies()
        self.currencies = currencies
        self.candlesticks = []
        self.currencies_quotation = None
        self.__currency_price_repository = CurrencyPriceRepository()

    def start_monitoring_currencies(self):
        '''
            Start currencies motiron method
        '''
        self.create_candles()
        self.monitor()

    def create_candles(self):
        for currency in self.currencies:
            for frequency in self.frequencies:
                self.candlesticks.append(self.create_candle(currency, frequency))
        return
            
    @classmethod
    def create_candle(cls, currency, frequency):
        '''
            Return a candlestick dict
        '''
        return {
            'exchange_id': currency[0],
            'frequency': frequency,
            'datetime': None,
            'open': None,
            'low': None,
            'high': None,
            'close': None
        }

    def monitor(self):
        '''
            Task to monitor currencies quotation updates
        '''
        schedule.every(1).seconds.do(self.get_currencies_quotation)
        schedule.every(1).seconds.do(self.update_candlesticks)
        schedule.every(60).seconds.do(self.save_candlesticks, frequency = 1)
        schedule.every(300).seconds.do(self.save_candlesticks, frequency = 5)
        schedule.every(600).seconds.do(self.save_candlesticks, frequency = 10)

        while True:
            schedule.run_pending()

    def get_currencies_quotation(self):
        '''
            Get current currency quotation
        '''
        controller = get_currencies_composer()
        response = controller.handler()['data']
        self.currencies_quotation = response
        print(f'Currencies Quotation: {self.currencies_quotation}')

    def update_candlesticks(self):
        '''
            Update candlesticks list
        '''
        for candlestick in self.candlesticks:
            for quotation in self.currencies_quotation:
                if candlestick['exchange_id'] == quotation['exchange_id']:
                    if candlestick['open'] == None:
                        candlestick['open'] = quotation['last']
                        candlestick['low'] = quotation['last']
                        candlestick['high'] = quotation['last']
                        candlestick['close'] = quotation['last']
                    else:
                        if candlestick['low'] > quotation['last']:
                            candlestick['low'] = quotation['last']
                        if candlestick['high'] < quotation['last']:
                            candlestick['high'] = quotation['last']
                        candlestick['close'] = quotation['last']
    
    def save_candlesticks(self, frequency):
        '''
            Save candlesticks into database
        '''
        for candlestick in self.candlesticks:
            if candlestick['frequency'] == frequency:
                candlestick['datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                print(f'Candlestick: {candlestick}')

                candlestick_converted = self.convert_candlestick_to_tuple(candlestick)
                self.__currency_price_repository.insert_currency_price(candlestick_converted)

                candlestick['open'] = None
                candlestick['low'] = None
                candlestick['high'] = None
                candlestick['close'] = None

    @classmethod
    def convert_candlestick_to_tuple(cls, candlestick):
        '''
            Convert candlestick dict to tuple
        '''
        return (
            candlestick['exchange_id'], 
            candlestick['frequency'], 
            candlestick['datetime'],
            float(candlestick['open']),
            float(candlestick['low']),
            float(candlestick['high']),
            float(candlestick['close'])
        )
