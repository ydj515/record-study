# Beautiful Soup

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

### example html
```html
<html> 
    <head> 
    </head> 
    <body> 
        <h1> 시장  
            <p id='fruits1' class='name' title='바나나'> 바나나 
                <span class = 'price'> 3000원 </span> 
                <span class = 'inventory'> 500개 </span> 
                <span class = 'store'> 가가가 </span> 
                <a href='http://test1'> url1 </a> 
            </p> 

            <p id='fruits2' class='name' title='귤'> 귤 
                <span class = 'price'> 2000원 </span> 
                <span class = 'inventory'> 100개 </span> 
                <span class = 'store'> 나나나</span> 
                <a href='http://test2'> url2 </a> 
            </p> 
            <p id='fruits3' class='name' title='파인애플'> 파인애플 
                <span class = 'price'> 5000원 </span> 
                <span class = 'inventory'> 10개 </span> 
                <span class = 'store'> 가가가</span> 
                <a href='http://test1' class='my'> url1 </a> 
            </p>
            <div> </div>
        </h1> 
    </body> 
</html>
```

### find()
- 조건에 해당하는 태그를 가져온다
- 중복이면 가정 첫번째 태그를 가져온다
```python
with open("example.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    first_p = soup.find("p")
    print(first_p)
    
    # <span class="price">의 span 태그만 뽑는다
    span = soup.find("span",{"class":"price"})
```

### findAll()
- 조건에 해당하는 태그들을 리스트에 담는다.
```python
with open("example.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    all_ps = soup.findAll("p")
    print(all_ps)
    
    # 리스트에 담기므로 for문 응용 가능
    for p in all_ps:
        print(p) # 하나씩 꺼내서 출력 하므로 [] 대괄호가 찍히지 않음
    
        a_tag = p.find("a")
        span = a_tag.find("span",{"class":"an_txt"})
    
        # .text를 붙히면 안의 값만 나옴
        print(span.text)
        print(span.text.strip()) # 공백 제거
```

### select()
- 조건에 해당하는 태그들을 리스트에 담는다.
- 1개더라도 리스트에 담는다
- 리스트로 반환
- find와는 다른 class, id 구분
- 구조적 위치로 접근 가능
```python
with open("example.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    all_spans = soup.select("span") # select로 div 태그들 추출
    print(all_spans)

    span = all_spans.select("span.an_txt") # span 태그중 class가 an_txt만 추출. 만약 하위 태그를 가진다면 하위태그들도 모두 추출
    my_id = all_spans.select("#fruits2") # fruits2라는 아이디를 가진 태그 추출. 만약 하위 태그를 가진다면 하위태그들도 모두 추출
    
    soup.select('p > span') # p 태그 바로 밑 자식 span
    soup.select('p span') # p 태그 밑 자손 span
    soup.select('p.name > span.price') #class가 name인 p 태그 바로 밑 class가 price인 자식 span
    soup.select('h1 .name > span.store') # class가 name인 h1 태그 밑 자손 class가 store인 자손 span

    # soup.select('태그[속성명 = 속성값]') 방식
    soup.select('span[class=price]') # span 태그의 class 속성이 price인 태그 추출


    # href 태그의 링크주소만 가져오기
    my = soup.select('a') # a 태그들을 list에 담기
    print(my[0][href]) # 첫번째 a 태그의 링크 주소만 가져오기

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

## File로 저장하기

### csv
- pandas를 이용하여 저장
```python
import pandas as pd # pandas 부르기

# result는 크롤링한 결과
# columns로 이름 지정
articles = pd.DataFrame(results, columns=['제목','작성자','작성일','본문', '댓글'])
articles.to_csv('./파일명.csv')
```

### JSON
- json 파일로 저장
```python
import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

```



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
    # result.encoding = None

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
https://m.blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221177292446&proxyReferer=https%3A%2F%2Fwww.google.com%2F