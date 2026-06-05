from utils.spark_session import get_spark
from pyspark.sql.functions import col

def silver():
    spark = get_spark()

    df = spark.read.parquet("data/bronze")

    df = df.dropna()
    df = df.filter(col("amount") > 0)

    df.write.mode("overwrite").parquet("data/silver")

if __name__ == "__main__":
    silver()
