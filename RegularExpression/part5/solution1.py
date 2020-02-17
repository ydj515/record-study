#-*- coding:utf-8 -*-

# 빈칸에 정규표현식을 적습니다.
# \s 공백 문자(스페이스, 탭, 뉴라인)
# \S 공백 문자를 제외한 문자
# \D 숫자를 제외한 문자
# \W 글자 대표 문자를 제외한 글자들(특수문자, 공백 등)
regex = r'\s'

# 주소록입니다. 이후 강의에서 모두 이 search_target을 사용합니다.
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))