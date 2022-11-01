import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="listing_4_07",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
)

# 인수에 context라는 이름을 지정하면 Airflow 태스크 콘텍스트라는 것을 의미한다.
def _print_context(**context):
    print(context)


print_context = PythonOperator(
    task_id="print_context", python_callable=_print_context, dag=dag
)
