# importando biblioteca e iniciando spark session
# iniciando e instanciando spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# importando dado
spark.sql("""
    CREATE TEMPORARY VIEW vw_device
    USING org.apache.spark.sql.json
    OPTIONS (path "/content/device/*.json")
""")

spark.sql("""
  CREATE TEMPORARY VIEW wv_subscription
  USING org.apache.spark.sql.json
  OPTIONS (path "/content/subscription/*.json")
""")

print(spark.catalog.listTables())

# selecionando dado
spark.sql("""SELECT * FROM vw_device LIMIT 10;""").show()

spark.sql("""SELECT * FROM wv_subscription LIMIT 10;""").show()

# novo dataframe = {join}
join_datasets = spark.sql("""
      SELECT dev.user_id,
              dev.model,
              dev.platform,
              subs.payment_method,
              subs.plan
      FROM vw_device AS dev
      INNER JOIN wv_subscription AS subs
      ON dev.user_id = subs.user_id
""")

# info
join_datasets.show()
join_datasets.printSchema()
join_datasets.count()