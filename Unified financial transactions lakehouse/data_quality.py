from utils.spark_session import get_spark

def dq():
    spark = get_spark()
    df = spark.read.parquet("data/silver")

    total = df.count()
    nulls = df.filter("amount IS NULL").count()

    assert total > 0, "No data"
    assert nulls == 0, "Null values found"

    print("Data Quality Passed")

if __name__ == "__main__":
    dq()
