from kafka import KafkaProducer
import time

# config Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# fetch data
file_path = "/Users/chester/Desktop/test/chester_test/testcases/streaming/raw.txt"
topic_name = "test-topic"

with open(file_path, "r") as file:
    for line in file:
        # send to Kafka
        producer.send(topic_name, line.strip().encode("utf-8"))
        print(f"Sent: {line.strip()}")
        time.sleep(1) 