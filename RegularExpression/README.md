# Regular Expression

## Grammar
|표현식                |설명                          |예시                         |
|----------------|-------------------------------|-----------------------------|
|`^`			 |문자열시작            |'Isn't this fun?'            |
|`$`          	 |문자열 종료            |"Isn't this fun?"            |
|`.`         	 |임의의 문자["는 넣을수 없음]|-- is en-dash, --- is em-dash|
|`*`         	 |앞 문자가 0개 이상의 개수가 존재할 수 있음|-- is en-dash, --- is em-dash|
|`+`         	 |앞 문자가 1개 이상의 개수가 존재할 수 있음|-- is en-dash, --- is em-dash|
|`?`         	 |앞 문자가 없거나 하나 있을 수 있음|-- is en-dash, --- is em-dash|
|`[]`          	 |문자의 집합이나 범위. -로 범위 나타냄. ^은 not|-- is en-dash, --- is em-dash|
|`{}`          	 |횟수 또는 범위|-- is en-dash, --- is em-dash|
|`()`            |괄호안의 문자를 하나의 문자로 인식함|-- is en-dash, --- is em-dash|
|`PIPE`          |패턴을 OR 연산을 수행할 때 사용|-- is en-dash, --- is em-dash|
|`/s`          	 |공백문자|-- is en-dash, --- is em-dash|
|`/S`          	 |공백 문자가 아닌 나머지 문자|-- is en-dash, --- is em-dash|
|`/w`          	 |알파벳이나 문자|-- is en-dash, --- is em-dash|
|`/W`          	 |알파벳이나 숫자를 제외한 문자|-- is en-dash, --- is em-dash|
|`/d`          	 |[0-9] 숫자|-- is en-dash, --- is em-dash|
|`/D`          	 |숫자를 제외한 모든 문자|-- is en-dash, --- is em-dash|
|`(?i)`          |대소문자를 구분하지 않음|-- is en-dash, --- is em-dash|

## 예시
### UserName
- 소문자, 숫자, _-포함
- 3글자 이상 16글자 이하  
`^[a-z0-9_-]{3,16}$`

### Password
- 소문자, 숫자, _-포함
- 6글자 이상 18글자 이하  
`^[a-z0-9_-]{6,18}$`

### Email
- 소문자, 숫자, _-포함
- @
- 소문자와 . 2글자 이상 6글자이하  
`^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$`

## <a href="https://programmers.co.kr/learn/courses/11">프로그래머스 정규표현식</a>
- <a href="https://github.com/ydj515/record-study/tree/master/RegularExpression/part1">1 정규표현식</a>
- <a href="https://github.com/ydj515/record-study/tree/master/RegularExpression/part2">2 대표문자(Meta sequence)</a>
- <a href="https://github.com/ydj515/record-study/tree/master/RegularExpression/part3">3 횟수 정하기(Quantifier)</a>
- <a href="https://github.com/ydj515/record-study/tree/master/RegularExpression/part4">4 고르기</a>
- <a href="https://github.com/ydj515/record-study/tree/master/RegularExpression/part5">5 더 알아보기</a>
- <a href="https://github.com/ydj515/record-study/tree/master/RegularExpression/part6">6 프로그래밍 언어별 정규표현식</a>