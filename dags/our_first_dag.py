from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2024, 7, 21, 19, 4),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo Hello World, this is the first task to be done'
    )
    
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo Hey, I am task2 and will be running after task 1'
    ) 
    
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo Hey, I am task3 and will be running after task 1'
    )

    
    # Task Dependency Method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task Dependency Method 2
    # task1 >> task2
    # task1 >> task3

    # Task Dependency Method 3
    task1 >> [task2,task3]
