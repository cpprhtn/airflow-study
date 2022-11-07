get_data = PythonOperator(
   task_id="get_data",
   python_callable=_get_data,
   op_kwargs={"output_path": "/tmp/wikipageviews.gz"}, # op_kwargs에 주어진 명령어가 호출 가능한 키워드 인수로 전달된다.
   dag=dag,
)