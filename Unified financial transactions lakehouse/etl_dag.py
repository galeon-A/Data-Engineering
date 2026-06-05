from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def run(cmd):
    os.system(cmd)

with DAG("financial_lakehouse_v2", start_date=datetime(2024,1,1), schedule_interval="@daily", catchup=False) as dag:

    t1 = PythonOperator(task_id="bronze", python_callable=lambda: run("python spark_jobs/bronze.py"))
    t2 = PythonOperator(task_id="silver", python_callable=lambda: run("python spark_jobs/silver.py"))
    t3 = PythonOperator(task_id="gold", python_callable=lambda: run("python spark_jobs/gold.py"))
    t4 = PythonOperator(task_id="fraud", python_callable=lambda: run("python spark_jobs/fraud_detection.py"))
    t5 = PythonOperator(task_id="dq", python_callable=lambda: run("python spark_jobs/data_quality.py"))

    t1 >> t2 >> t3 >> [t4, t5]
