from elasticsearch import Elasticsearch
import time

# use this for testing ES connection
es = Elasticsearch(["http://elastic:elastic-password@127.0.0.1:9200"], verify_certs=False)

if es.ping():
    print('Yay Connect')
    es.indices.delete(index="test_index")
    es.indices.create(index="test_index")
    print('Created index')
    doc = {
        "test": "test"
    }
    resp = es.index(index="test_index", body=doc)
    print(resp['result'])
else:
    print('Awww it could not connect!')
