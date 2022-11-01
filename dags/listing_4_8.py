import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="listing_4_08",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
)


def _print_context(**context):
    start = context["execution_date"]    # context로부터 execution_date 추출
    end = context["next_execution_date"]
    print(f"Start: {start}, end: {end}")


print_context = PythonOperator(
    task_id="print_context", 
    python_callable=_print_context, 
    dag=dag
)

# 출력 예:
# Start: 2019-07-13T14:00:00+00:00, end: 2019-07-13T15:00:00+00:00