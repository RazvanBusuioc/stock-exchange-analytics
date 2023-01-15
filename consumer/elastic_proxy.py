from elasticsearch import Elasticsearch
from config import Config

class ElasticProxy:
    def __init__(self) -> None:
        print(f"http://{Config.ELASTIC_USER}:{Config.ELASTIC_PASSWORD}@{Config.ELASTIC_HOST}:{Config.ELASTIC_PORT}")
        self.es = Elasticsearch([f"http://{Config.ELASTIC_USER}:{Config.ELASTIC_PASSWORD}@{Config.ELASTIC_HOST}:{Config.ELASTIC_PORT}"], verify_certs=False)
        print(self.es.info())
        if self.es.ping():
            print('Yay Connected to Elasticsearch')
        else:
            print('Awww it could not connect to Elasticsearch!')
        self.indexes = set()

    def store_message(self, message):
        print(message[0])
        print(message[6])
        print(type(message[6]))
        index = message[0]
        doc = message[6]
        if index not in self.indexes:
            if not self.es.indices.exists(index=index):
                self.es.indices.create(index=index)
            self.indexes.add(index)
        resp = self.es.index(index=index, body=doc)
        print(resp['result'])
