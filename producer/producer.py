from kafka import KafkaProducer
from stock_exchange import get_stock_exchange_data
from config import Config
import json
import time

def init_producer():
    producer = KafkaProducer(bootstrap_servers=Config.KAFKA_HOST + ':' + str(Config.KAFKA_PORT),
                             value_serializer=lambda data: json.dumps(data).encode('utf-8'))
    print('Kafka Producer has been initiated...')
    return producer


def produce_data_loop(producer):
    while True:
        data = get_stock_exchange_data()
        for symbol in data:
            topic = 'finance.' + symbol
            producer.send(topic, data[symbol])
            producer.flush()
            message = 'Produced message on topic {}.'.format(topic)
            print(message)
        print()