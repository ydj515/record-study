#-*- coding:utf-8 -*-

# 본 문제는 실행만하면 통과하는 문제입니다.
regex = r'\d+[- ]?\d+[- ]?\d+'

search_target = '''이상한 전화번호 0030589-5-95826
Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

#아래 부분은 본 강의에서 다루지 않습니다.
import re
result=re.findall(regex,search_target)
print(result)