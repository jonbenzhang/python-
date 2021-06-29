from pyspark.sql import SparkSession,DataFrame
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
# df = spark.read.json("examples/src/main/resources/people.json")
df = spark.read.json("./people.json")
df.show()
df.printSchema()