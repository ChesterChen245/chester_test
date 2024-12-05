# clone spark with docker
docker pull bitnami/spark

# kickoff spark
docker run -it --name spark-container \
  -p 4040:4040 -p 8080:8080 -p 7077:7077 \
  bitnami/spark /bin/bash


