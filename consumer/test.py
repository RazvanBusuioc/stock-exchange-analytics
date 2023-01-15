from elasticsearch import Elasticsearch

# use this for testing ES connection
es = Elasticsearch(["http://localhost:9200"], basic_auth=("elastic", "elastic-password"), verify_certs=False)
if es.ping():
    print('Yay Connect')
else:
    print('Awww it could not connect!')
