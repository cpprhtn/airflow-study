# python에게 execution_date라는 인수가 필요하다는 것을 선언한다.
# context 인수에서 캡처되지 않는다.
def _get_data(execution_date, **context):
   year, month, day, hour, *_ = execution_date.timetuple()
   # ...