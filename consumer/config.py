import os

class Config:
    KAFKA_HOST = os.getenv('KAFKA_HOST')
    KAFKA_PORT = os.getenv('KAFKA_PORT')
