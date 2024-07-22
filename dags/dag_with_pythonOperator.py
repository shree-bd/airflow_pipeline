from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(name, age):
    print(f"Hello World!! My name is {name}, and I am {age} years old")

with DAG(
    dag_id='dag_with_python_operator_v2',
    default_args=default_args,
    description='This is our first dag that we write using Python Operator',
    start_date=datetime(2024, 7, 21, 19, 40),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id='Greet',
        python_callable=greet,
        op_kwargs={'name': 'Tom', 'age': 20}
    )

    task1
