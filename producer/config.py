import os

class Config:
    KAFKA_HOST = os.getenv('KAFKA_HOST')
    KAFKA_PORT = os.getenv('KAFKA_PORT')
    STOCK_API_URL = 'http://query1.finance.yahoo.com/v10/finance/quoteSummary/'
    COMPANY_NAME_API_URL = 'https://query2.finance.yahoo.com/v1/finance/search'
    STOCK_API_USER_AGENT_HEADER = { 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}
