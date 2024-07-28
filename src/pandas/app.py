# import e configuração
# import e configuração
from pyspark.sql import SparkSession
builder = SparkSession.builder.appName("app")

builder = builder.config("spark.sql.execution.arraw.pyspark.enabled", "true")
builder.getOrCreate()
print(builder)


# padas in spark 
import pyspark.pandas as ps

# lendo arquivos
get_device = ps.read_json("/content/device/*.json")
get_subscription = ps.read_json("/content/subscription/*.json")

print(get_device)
print(get_subscription)

get_device.info()
get_subscription.info()

# get plan
get_device.spark.explain(mode="formatted")
get_subscription.spark.explain(mode="formatted")
