from utils.spark_session import get_spark
from pyspark.sql.functions import sum as _sum, avg

def gold():
    spark = get_spark()

    df = spark.read.parquet("data/silver")

    agg = df.groupBy("customer_id").agg(
        _sum("amount").alias("total_spent"),
        avg("amount").alias("avg_ticket_size")
    )

    agg.write.mode("overwrite").parquet("data/gold")

if __name__ == "__main__":
    gold()
