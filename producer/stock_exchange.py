import requests
import time
from companies import companies_symbols
from config import Config
from datetime import datetime

class API:
    
    # call stock exchange API for all the companies
    # return a dict structured like this: { company_symbol: json_data_for_company }
    def get_stock_exchange_data(self):
        result = {}
        for company_symbol in companies_symbols:
            data = self.get_stock_exchange_data_for_symbol(company_symbol)
            result[company_symbol] = data
        return result

    def get_stock_exchange_data_for_symbol(self,company_symbol):
        res = requests.get(
            Config.STOCK_API_URL + company_symbol, 
            headers = Config.STOCK_API_USER_AGENT_HEADER, 
            params  = {'modules' : 'financialData,assetProfile'}
        )
        stockData = res.json()['quoteSummary']['result'][0]['financialData']

        res = requests.get(
            Config.COMPANY_NAME_API_URL,
            headers = Config.STOCK_API_USER_AGENT_HEADER, 
            params  = {'q' : company_symbol}
        )
        stockData['companyName'] = res.json()['quotes'][0]['shortname']
        stockData['time'] = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y, %H:%M:%S")
        return stockData