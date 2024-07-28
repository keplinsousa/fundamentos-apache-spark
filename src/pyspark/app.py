# importando biblioteca e iniciando spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# carregando dado
df_device = spark.read.json("/home/coder/project/fundamentos-apache-spark/docs/files/device/device_2022_6_7_19_39_24.json")
df_device.show()

# schema
df_device.printSchema()

# colunas
print(df_device.columns)

# linhas
print(df_device.count())

# selecionar colunas
df_device.select("manufacturer", "model", "platform").show()
df_device.selectExpr("manufacturer", "model", "platform as type").show()

# filtro
df_device.filter(df_device.manufacturer == "Xiamomi").show()

# group by
df_device.groupBy("manufacturer").count().show()