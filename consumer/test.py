from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection

# use this for testing ES connection
es = Elasticsearch(["http://elastic:elastic-password@127.0.0.1:9200"], verify_certs=False)

if es.ping():
    print('Yay Connect')
else:
    print('Awww it could not connect!')
