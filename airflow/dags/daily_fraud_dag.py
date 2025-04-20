from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import psycopg2
import pandas as pd

def extract_frauds():
    conn = psycopg2.connect("dbname=fraud user=user password=password")
    df = pd.read_sql("SELECT * FROM fraud_transactions WHERE detected_at >= now() - interval '1 day'", conn)
    df.to_csv("/tmp/frauds_report.csv", index=False)
    print("✅ Rapport des fraudes généré")

with DAG("daily_fraud_report",
         start_date=datetime(2023, 1, 1),
         schedule_interval="@daily",
         catchup=False) as dag:

    task = PythonOperator(
        task_id="generate_daily_report",
        python_callable=extract_frauds
    )
