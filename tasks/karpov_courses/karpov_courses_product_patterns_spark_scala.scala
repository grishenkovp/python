// Databricks notebook source
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._

// COMMAND ----------

val path = "/FileStore/tables/data_two_columns.csv"
val df = spark.read.option("delimiter", ",").option("header", "true").csv(path)
df.show(7)

// COMMAND ----------

val df_group = df.groupBy("invoiceno").agg(collect_set("stockcode").as("list_stockcode"))
df_group.show(7)

// COMMAND ----------

val df_group_filter = df_group.filter(size(df_group("list_stockcode"))>1)
df_group_filter.show(7)

// COMMAND ----------

val combinationsStockСodeUDF= udf((l: Array[String]) => l.sorted.toSeq.combinations(2).toList)

// COMMAND ----------

val df_group_combinations = df_group_filter.select(col("invoiceno"),combinationsStockСodeUDF(col("list_stockcode")).as("combinations_stockcode"))
df_group_combinations.show(7)

// COMMAND ----------

val df_final = df_group_combinations.select(explode(col("combinations_stockcode")).as("couple_stockcode"))
df_final.groupBy("couple_stockcode").count().sort(col("count").desc).show(10)
