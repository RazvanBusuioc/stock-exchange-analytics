import os

class Config:
    KAFKA_HOST = os.getenv('KAFKA_HOST')
    KAFKA_PORT = os.getenv('KAFKA_PORT')
    ELASTIC_HOST = os.getenv('ELASTIC_HOST')
    ELASTIC_PORT = os.getenv('ELASTIC_PORT')
    ELASTIC_USER = os.getenv('ELASTIC_USER')
    ELASTIC_PASSWORD = os.getenv('ELASTIC_PASSWORD')
