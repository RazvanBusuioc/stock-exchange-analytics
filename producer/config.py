import os

class Config:
    KAFKA_HOST = "localhost" # os.getenv('KAFKA_HOST')
    KAFKA_PORT = 9092 #os.getenv('KAFKA_PORT')
    STOCK_API_URL = 'http://query1.finance.yahoo.com/v10/finance/quoteSummary/'
    STOCK_API_USER_AGENT_HEADER = { 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}
