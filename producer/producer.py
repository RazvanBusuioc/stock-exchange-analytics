from kafka import KafkaProducer
from stock_exchange import API
from config import Config
import json

class Producer:

    def __init__(self) -> None:
        self.api = API()
        self.kafka_producer = KafkaProducer(
            bootstrap_servers=Config.KAFKA_HOST + ':' + str(Config.KAFKA_PORT),
            value_serializer=lambda data: json.dumps(data).encode('utf-8')
        )
        print('Kafka Producer has been initiated...')
    
    def produce_data_loop(self) -> None:
        while True:
            try:
                data = self.api.get_stock_exchange_data()
                for symbol in data:
                    topic = 'finance.' + symbol
                    self.kafka_producer.send(topic, data[symbol])
                    self.kafka_producer.flush()
                    message = 'Produced message on topic {}'.format(topic)
                    print(message)
                print()
            except:
                pass
            
            