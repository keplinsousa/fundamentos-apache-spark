# https://spark.apache.org/docs/latest/submitting-applications.html

```shell
spark-submit --help
```

```shell
--deploy-mode
# cluster = o driver é executado em um dos nós de trabalho
# [client | default] = o driver é executado localmente onde você está enviando o aplicativo ~ não usado para produção

--master
# yarn = cluster resources
# mesos = mesos://host:port
# standalone = spark://host:port
# kubernetes = k8s://host:port
# local = local
```

```shell
option | description
--driver-memory	| # memória a ser usada pelo driver spark
--driver-cores | # núcleos de CPU a serem usados ​​pelo driver spark
--num-executors	|#  o número total de executores a serem usados
--executor-memory | # quantidade de memória a ser usada para o processo executor
--executor-cores | # número de núcleos de CPU a serem usados ​​para o processo executor
--total-executor-cores | # o número total de núcleos executores a serem usados
```

```shell
# scala
./bin/spark-submit \
--master yarn \
--deploy-mode cluster \
--conf "spark.sql.shuffle.partitions=20000" \
--jars "dependency1.jar,dependency2.jar"
--class com.sparkbyexamples.WordCountExample \
spark-by-examples.jar 

# pyspark
./bin/spark-submit \
   --master yarn \
   --deploy-mode cluster \
   wordByExample.py
```

```shell
spark-submit \
    /Users/luanmorenomaciel/GitHub/series-spark/src/first_app.py
```