get_data = PythonOperator(
   task_id="get_data",
   python_callable=_get_data,
   op_args=["/tmp/wikipageviews.gz"], # op_args를 사용하여 콜러블 함수에 추가 변수를 제공한다.
   dag=dag,
)