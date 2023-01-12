# Elasticsearch Setup

docker network create elastic
docker run -d -e ELASTIC_PASSWORD=elastic-password --name es-container --net elastic -p 9200:9200 -it docker.elastic.co/elasticsearch/elasticsearch:8.5.3

# Connect to ES with

# - node: https://localhost:9200
# - rejectUnauthorized: false (we can enable certificate if needed, see https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
# - user: elastic
# - password: elastic-password