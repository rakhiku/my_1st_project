from pyspark.sql import SparkSession
from config import getProperties
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

para_dict=getProperties("ABC.properties")


rdd2 = spark.sparkContext.textFile(para_dict['input_partition'])
print(rdd2.collect())

