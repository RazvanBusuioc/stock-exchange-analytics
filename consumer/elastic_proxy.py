from elasticsearch import Elasticsearch
from config import Config

class ElasticProxy:

    # TODO connect to Elastic
    def __init__(self) -> None:
        self.es = Elasticsearch(["http://"+Config.ELASTIC_HOST+":"+Config.ELASTIC_PORT], basic_auth=("elastic", "elastic-password"), verify_certs=False)
        if self.es.ping():
            print('Yay Connect')
        else:
            print('Awww it could not connect!')

    #TODO store message.value in Elastic
    def store_message(self, message):
        pass
        # print(message.value)