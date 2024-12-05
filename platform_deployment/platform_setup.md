# config kafka & spark
refer to docker-compose.yaml under the same folder

# setup kafka and spark
```shell
cd /chester_test
docker-compose up -d
```

# kickoff docker contianer
docker run -it --name spark-container \
  -p 4040:4040 -p 8080:8080 -p 7077:7077 \
  bitnami/spark /bin/bash

# kickoff zookeeper
docker run -d --name zookeeper -p 2181:2181 \
  -e ZOOKEEPER_CLIENT_PORT=2181 \
  -e ZOOKEEPER_TICK_TIME=2000 \
  confluentinc/cp-zookeeper

# kickoff kafka
docker run -d --name kafka -p 9092:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  --link zookeeper:zookeeper \
  confluentinc/cp-kafka


