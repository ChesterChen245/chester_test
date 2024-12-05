# from pyspark.sql import SparkSession
# from pyspark.streaming import StreamingContext
# # from pyspark.streaming.kafka import KafkaUtils

# # initiate SparkSession & StreamingContext
# spark = SparkSession.builder \
#     .appName("KafkaSparkStreaming") \
#     .getOrCreate()

# sc = spark.sparkContext
# ssc = StreamingContext(sc, 5)  # batch every 5s.

# # Kafka config
# kafka_params = {"metadata.broker.list": "localhost:9092"}
# kafka_topic = "test-topic"

# # fetch data from Kafka
# # kafka_stream = KafkaUtils.createDirectStream(ssc, [kafka_topic], kafka_params)
# df=spark.readStream \
#     .format("kafka") \
#     .option("kafka.bootstrap.servers", "localhost:9092") \
#     .option("subscribe", kafka_topic) \
#     .load()

# # data processing
# # lines = kafka_stream.map(lambda msg: msg[1])  # read data
# query = df.writeStream \
#     .outputMode("append") \
#     .format("console") \
#     .start()
# # data print
# # lines.pprint()

# #Spark Streaming
# ssc.start()
# ssc.awaitTermination()

from pyspark.sql import SparkSession

# 创建 SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

# Kafka 配置
kafka_bootstrap_servers = "localhost:9092"
kafka_topic = "test-topic"

# 从 Kafka 读取数据
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .load()

# 数据处理：将值转换为字符串
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# 设置查询，将数据输出到控制台
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# 等待查询终止
query.awaitTermination()