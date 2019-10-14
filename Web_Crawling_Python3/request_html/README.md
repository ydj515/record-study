# request_html 이용

## install
- python 3.6버전만 된다고 나와있는데 3.7 사용중이지만 아직 별다른 문제점이 발견되지 않았다.

```
pip install requests-html
```


## 사용법

### 기본
```python
from requests_html import HTMLSession

url = "https://python.org/"
session = HTMLSession()
r = session.get(url)
```

### response 코드, 태크 출력
```python

print(r) # <Response [200]>
print(r.html.links) # a 태그의 링크를 모두 출력
print(r.html.absolute_links)
```

### html 태그 찾기
```python
h3_tag = r.html.find('h3') # 'requests_html.Element' type
print(h3_tag) # [<Element 'h3' >, <Element 'h3' >]

# 첫번째 태그만 찾기
h3_tag = r.html.find('h3', first=True) # 'requests_html.Element' type
print(h3_tag) # [<Element 'h3' >]
print(h3_tag.text) # 내용만 출력
```

### class로 찾기
```python
h3_tag = r.html.find('.center') # 'requests_html.Element' type
print(h3_tag) # [<Element 'h3' >, <Element 'h3' >]
```

### css selector
```python
r = session.get('https://github.com/')
sel = 'body > div.application-main > div.jumbotron.jumbotron-codelines > div > div > div.col-md-7.text-center.text-md-left > p'
print(r.html.find(sel, first=True).text)
```

### XPath
```python
r.html.xpath('/html/body/div[1]/a')
```

### JavaScript... r.html.render() 이 함수를 사용하면 JavaScript코드 긁을 수 있다.
```python
r = session.get('https://pythonclock.org')
a = r.html.search('Python 2.7 will retire in...{}Enable Guido Mode')[0]
print(a)

r.html.render()
b = r.html.search('Python 2.7 will retire in...{}Enable Guido Mode')[0]
print(b)
```


[출처]  
https://github.com/psf/requests-html
