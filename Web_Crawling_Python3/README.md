# Web Crawling Python3

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


## 함수

### find()
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
### findAll()
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


## JSON
- Javascript Object Notation
- tree 구조
- key : value
- 자바스크립트에서 데이터 객체를 표현하는 방법
 
| <center>name</center> | <center>age</center> | <center>math</center> | <center>english</center> |
|:--------|:--------:|:--------:|:--------:|
|**dongjin** | <center>20</center> | <center>50</center> | <center>99</center> |
|**yoo**     | <center>25</center> | <center>75</center> | <center>99</center> |

```json
[
  {"name":"dongjin", "age":"20", "math":"50", "english":"99"},
  {"name":"yoo", "age":"25", "math":"75", "english":"99"}
]
```

### JSON tree
- json의 형식의 데이터를 뷰어로 보여준다.
- http://jsonviewer.stack.hu/

## Tag & Property 
### Tag
- 태그
- ul태그, li태그, div태그...

### property
- 속성
- class, id, href, title, src...

### property value
- 속성값
- class="greet">에서 greet이 속성값

### Example
```html
<a href="www.naver.com">
```
여기 위의 코드에서 **tag** : a, **property** : href, **property value** : www.naver.com


## encoding
- 한국어 페이지의 경우 EUC-KR이 많기 때문에 이를 크롤링 할 떄 원하는 값을 못 가져올 수 있음
- 따라서 UTF-8로 변환해 주는 작업이 필요하다
```python
def get_bs_obj():
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    result = requests.get(url)

    # 현재 페이지가 EUC-KR로 되어 있기 때문에 utf-8로 변환을 먼저 해준다.
    print(result.encoding)
    result.encoding = 'utf-8'
    
    bs_obj = BeautifulSoup(result.content, "html.parser")

    return bs_obj
```

- 간혹 가다가 console에서 UTF-8로 안될 경우 밑의 코드를 추가한다
```python
# -*- encoding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
```

- visual code에서 밑의 처럼 되어있는지 확인  
![1](https://user-images.githubusercontent.com/32935365/65445744-dbaf2180-de6d-11e9-8f03-a291aef3f3c3.PNG)  




[출처]  
https://www.youtube.com/playlist?list=PLAdQRRy4vtQRzdg7D9n1rkDp9DIeWpBQ9