import requests
from companies import companies_symbols
from config import Config

# call stock exchange API for all the companies
# return a dict structured like this: { company_symbol: json_data_for_company }
def get_stock_exchange_data():
    result = {}
    for company_symbol in companies_symbols:
        data = get_stock_exchange_data_for_symbol(company_symbol)
        result[company_symbol] = data
    return result

def get_stock_exchange_data_for_symbol(company_symbol):
    res = requests.get(
        Config.STOCK_API_URL + company_symbol, 
        headers = Config.STOCK_API_USER_AGENT_HEADER, 
        params  = {'modules' : 'financialData'}
    )
    return res.json()['quoteSummary']['result'][0]['financialData']