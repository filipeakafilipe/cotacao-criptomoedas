from src.main.tasks.monitor_currencies import CurrenciesMonitoring
import unittest

class Test(unittest.TestCase):

    def test_create_candles(self):
        ''' Test if Create Candles function initialized candles currectly '''

        currencies_monitoring = CurrenciesMonitoring([(121, 'USDT_BTC'), 
        (149, 'USDT_ETH'), 
        (689, 'USDT_SOL')])
        currencies_monitoring.frequencies = [1, 5, 10]

        candlesticks = [{'exchange_id': 121, 'frequency': 1, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}, 
        {'exchange_id': 121, 'frequency': 5, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}, 
        {'exchange_id': 121, 'frequency': 10, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}, 
        {'exchange_id': 149, 'frequency': 1, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}, 
        {'exchange_id': 149, 'frequency': 5, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}, 
        {'exchange_id': 149, 'frequency': 10, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}, 
        {'exchange_id': 689, 'frequency': 1, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}, 
        {'exchange_id': 689, 'frequency': 5, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}, 
        {'exchange_id': 689, 'frequency': 10, 'datetime': None, 'open': None, 'low': None, 'high': None, 'close': None}]

        currencies_monitoring.create_candles()

        self.assertEquals(currencies_monitoring.candlesticks, candlesticks)

    def test_update_candlesticks(self):
        ''' Test if Update Candlesticks function updated multiple currencies, for multiple frequencies correctly '''

        currencies_monitoring = CurrenciesMonitoring([(121, 'USDT_BTC'), 
        (149, 'USDT_ETH'), 
        (689, 'USDT_SOL')])
        currencies_monitoring.frequencies = [1, 5, 10]
        
        candlesticks = [{'exchange_id': 121, 'frequency': 1, 'datetime': None, 'open': '37416.19998998', 'low': '37416.19998998', 'high': '37416.19998998', 'close': '37416.19998998'}, 
        {'exchange_id': 121, 'frequency': 5, 'datetime': None, 'open': '37416.19998998', 'low': '37416.19998998', 'high': '37416.19998998', 'close': '37416.19998998'}, 
        {'exchange_id': 121, 'frequency': 10, 'datetime': None, 'open': '37416.19998998', 'low': '37416.19998998', 'high': '37416.19998998', 'close': '37416.19998998'}, 
        {'exchange_id': 149, 'frequency': 1, 'datetime': None, 'open': '2675.03187848', 'low': '2675.03187848', 'high': '2675.03187848', 'close': '2675.03187848'}, 
        {'exchange_id': 149, 'frequency': 5, 'datetime': None, 'open': '2675.03187848', 'low': '2675.03187848', 'high': '2675.03187848', 'close': '2675.03187848'}, 
        {'exchange_id': 149, 'frequency': 10, 'datetime': None, 'open': '2675.03187848', 'low': '2675.03187848', 'high': '2675.03187848', 'close': '2675.03187848'}, 
        {'exchange_id': 689, 'frequency': 1, 'datetime': None, 'open': '108.62844545', 'low': '108.62844545', 'high': '108.62844545', 'close': '108.62844545'}, 
        {'exchange_id': 689, 'frequency': 5, 'datetime': None, 'open': '108.62844545', 'low': '108.62844545', 'high': '108.62844545', 'close': '108.62844545'}, 
        {'exchange_id': 689, 'frequency': 10, 'datetime': None, 'open': '108.62844545', 'low': '108.62844545', 'high': '108.62844545', 'close': '108.62844545'}]

        currencies_monitoring.currencies_quotation = [{'exchange_id': 121, 'currency': 'USDT_BTC', 'last': '37416.19998998'}, 
        {'exchange_id': 149, 'currency': 'USDT_ETH', 'last': '2675.03187848'}, 
        {'exchange_id': 689, 'currency': 'USDT_SOL', 'last': '108.62844545'}]

        currencies_monitoring.create_candles()
        currencies_monitoring.update_candlesticks()

        self.assertEquals(currencies_monitoring.candlesticks, candlesticks)

    def test_update_candlesticks_multiple_quotations(self):
        ''' Test if Update Candlesticks function updated multiple currencies, for multiple quotation correctly '''

        currencies_monitoring = CurrenciesMonitoring([(121, 'USDT_BTC'), 
        (149, 'USDT_ETH'), 
        (689, 'USDT_SOL')])
        currencies_monitoring.frequencies = [1]
        
        candlesticks = [{'exchange_id': 121, 'frequency': 1, 'datetime': None, 'open': '37416.19998998', 'low': '37416.19998998', 'high': '37420.19998998', 'close': '37418.19998998'}, 
        {'exchange_id': 149, 'frequency': 1, 'datetime': None, 'open': '2675.03187848', 'low': '2675.03187848', 'high': '2680.03187848', 'close': '2677.03187848'}, 
        {'exchange_id': 689, 'frequency': 1, 'datetime': None, 'open': '108.62844545', 'low': '108.62844545', 'high': '115.62844545', 'close': '115.62844545'}]

        currencies_monitoring.create_candles()

        currencies_monitoring.currencies_quotation = [{'exchange_id': 121, 'currency': 'USDT_BTC', 'last': '37416.19998998'}, 
        {'exchange_id': 149, 'currency': 'USDT_ETH', 'last': '2675.03187848'}, 
        {'exchange_id': 689, 'currency': 'USDT_SOL', 'last': '108.62844545'}]

        currencies_monitoring.update_candlesticks()

        currencies_monitoring.currencies_quotation = [{'exchange_id': 121, 'currency': 'USDT_BTC', 'last': '37420.19998998'}, 
        {'exchange_id': 149, 'currency': 'USDT_ETH', 'last': '2680.03187848'}, 
        {'exchange_id': 689, 'currency': 'USDT_SOL', 'last': '110.62844545'}]

        currencies_monitoring.update_candlesticks()

        currencies_monitoring.currencies_quotation = [{'exchange_id': 121, 'currency': 'USDT_BTC', 'last': '37418.19998998'}, 
        {'exchange_id': 149, 'currency': 'USDT_ETH', 'last': '2677.03187848'}, 
        {'exchange_id': 689, 'currency': 'USDT_SOL', 'last': '115.62844545'}]

        currencies_monitoring.update_candlesticks()

        self.assertEquals(currencies_monitoring.candlesticks, candlesticks)
