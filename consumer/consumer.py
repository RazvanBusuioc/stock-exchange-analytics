from kafka import KafkaConsumer
from config import Config
from json import loads

def init_consumer():
    consumer = KafkaConsumer(bootstrap_servers=Config.KAFKA_HOST + ':' + str(Config.KAFKA_PORT),
                             value_deserializer=lambda data: loads(data.decode('utf-8')),
                             auto_offset_reset='earliest') # not sure we need this here
    print('Kafka Consumer has been initiated...')
    return consumer


consumer = init_consumer()
consumer.subscribe(['finance.amzn', 'finance.aapl'])
for message in consumer:
    print (message.topic)
