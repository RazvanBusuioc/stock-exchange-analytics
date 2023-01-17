# Setup Tutorial

1. sudo sysctl -w vm.max_map_count=262144
2. # make sure old (not updated) volumes are deleted
3. docker-compose up -d
4. $ Check Kafka interface at http://localhost:8080/ui/docker-kafka-server/topic

# Connect to ES with

# - node: https://localhost:9200
# - rejectUnauthorized: false (we can enable certificate if needed, see https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
# - user: elastic
# - password: elastic-password

# Kafka and Kafka Interface Setup

# Interface: http://localhost:8080/
# Kafka Broker: http://localhost:9092/

# Team

Busuioc Gabriel-Răzvan
Fodor Bianca-Mihaela
Roman Adrian
Șerboi Florea-Dan