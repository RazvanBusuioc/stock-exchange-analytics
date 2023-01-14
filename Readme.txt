# Setup Tutorial

1. sudo sysctl -w vm.max_map_count=262144
2. # make sure old (not updated) volumes are deleted
3. docker-compose up -d
4. $ Check Kafka interface at http://localhost:8080/ui/docker-kafka-server/topic

TO DOS
Need to Have:
- add ES indexing on consumer

Nice to have:
- Kafka Auth
- Producer/Consumer scaling