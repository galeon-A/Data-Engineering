from utils.spark_session import get_spark
from pyspark.sql.functions import col, count

def fraud():
    spark = get_spark()
    df = spark.read.parquet("data/silver")

    flagged = df.filter(col("amount") > 3000)

    velocity = df.groupBy("customer_id").agg(count("*").alias("tx_count"))
    risky = velocity.filter(col("tx_count") > 5)

    flagged.write.mode("overwrite").parquet("data/gold/fraud_flagged")
    risky.write.mode("overwrite").parquet("data/gold/velocity_risk")

if __name__ == "__main__":
    fraud()
