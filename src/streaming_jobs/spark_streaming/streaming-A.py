from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
# from pyspark.streaming.kafka import KafkaUtils

# initiate SparkSession & StreamingContext
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

sc = spark.sparkContext
ssc = StreamingContext(sc, 5)  # batch every 5s.

# Kafka config
kafka_params = {"metadata.broker.list": "localhost:9092"}
kafka_topic = "test-topic"

# fetch data from Kafka
# kafka_stream = KafkaUtils.createDirectStream(ssc, [kafka_topic], kafka_params)
kafka_stream=spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", kafka_topic) \
    .load()

# data processing
# lines = kafka_stream.map(lambda msg: msg[1])  # read data
kafka_stream.show()

# data print
# lines.pprint()

#Spark Streaming
ssc.start()
ssc.awaitTermination()