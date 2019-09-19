# WebCrawling-Python

## Beautiful Soup 설치
```
pip install beautifulsoup4
```

### import
```
from bs4 import BeautifulSoup
```
```
import bs4
```

### HTML file Open
```python
with open("example.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
```

### get URL
```python
import urllib.request
import urllib.parse

with urllib.request.urlopen("https://www.naver.com") as response:
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
```
```python 
import requests

r = requests.get("https://www.naver.com")
r.status_code # 상태 코드
r.headers['content-type'] # content type
r.encoding # encoding
r.text
print(r.text) # html tag 출력
```

### 함수
#### find()
- 조건에 해당하는 태그를 가져온다
- 중복이면 가정 첫번째 태그를 가져온다
```
with open("example.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    first_div = soup.find("div")
    print(first_div)
    
    # <ul class="an_l">의 ul 태그만 뽑는다
    ul = soup.find("ul",{"class":"an_l"})
```
#### findAll()
- 조건에 해당하는 태그들을 리스트에 담는다.
```python
with open("example.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    all_divs = soup.findAll("div")
    print(all_divs)
    
    # 리스트에 담기므로 for문 응용 가능
    for li in all_divs:
        print(li) # 하나씩 꺼내서 출력 하므로 [] 대괄호가 찍히지 않음
    
        a_tag = li.find("a")
        span = a_tag.find("span",{"class":"an_txt"})
    
        # .text를 붙히면 안의 값만 나옴
        print(span.text)
```

[출처]  
https://www.youtube.com/playlist?list=PLAdQRRy4vtQRzdg7D9n1rkDp9DIeWpBQ9