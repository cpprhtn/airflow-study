# 키워드 인수는 두 개의 애스터리스크(**)로 표시하면 캡처된다. 
# 그리고 캡처 인수의 이름을 kwargs에 지정한다.
def _print_context(**kwargs):
   print(kwargs)