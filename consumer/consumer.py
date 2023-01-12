from kafka import KafkaConsumer
from config import Config
from json import loads
from elastic_proxy import ElasticProxy
import time

class Consumer:
    def __init__(self) -> None:
        self.elastic_proxy = ElasticProxy()
        self.kafka_consumer = KafkaConsumer(
            bootstrap_servers=Config.KAFKA_HOST + ':' + str(Config.KAFKA_PORT),
            value_deserializer=lambda data: loads(data.decode('utf-8')),
            auto_offset_reset='earliest'
        )
        print('Kafka Consumer has been initiated...')
    
    def subscribe(self, topics):
        self.kafka_consumer.subscribe(topics)
        print('Kafka Consumer has subscribed to topics ', topics)

    def consume_data_loop(self) -> None:
        for message in self.kafka_consumer:
            self.elastic_proxy.store_message(message)
