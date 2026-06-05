from utils.spark_session import get_spark

def bronze():
    spark = get_spark()

    df = spark.read.option("header", True).csv("data/raw/transactions.csv")

    df.write.mode("overwrite").parquet("data/bronze")

if __name__ == "__main__":
    bronze()
