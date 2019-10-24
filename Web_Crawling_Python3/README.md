# Web Crawling Python3

## Beautiful Soup 이용
- https://github.com/ydj515/record-study/tree/master/Web_Crawling_Python3/BeautifulSoup4

## Selenium 이용
- https://github.com/ydj515/record-study/tree/master/Web_Crawling_Python3/Selenium

## request_html 이용
- https://github.com/ydj515/record-study/tree/master/Web_Crawling_Python3/request_html

## Naver API Key

### 1. 애플리케이션 등록
- 밑의 url로 접속  
https://developers.naver.com/products/login/api/  
![1](https://user-images.githubusercontent.com/32935365/67477587-58afff80-f695-11e9-8fa3-5934cfe52d3e.PNG)


- 비로그인 오픈 API 서빗 환경을 등록
    - com.hororok처럼 패키지명을 적어야됨!  
![3333](https://user-images.githubusercontent.com/32935365/67477549-45049900-f695-11e9-9970-6698d2e13c9b.PNG)


### 2. ID & Secret
- [내 애플리케이션]-[프로젝트명]  
![2](https://user-images.githubusercontent.com/32935365/67477614-6bc2cf80-f695-11e9-906e-2defeb8d77a9.PNG)

### 3. 사용법
```python
import requests
from bs4 import BeautifulSoup

client_id = "CBtyju_UT3NjM1k0Gxk3" # 내 ID
client_secret = "lyIS61mwQJ" # 내 secret

encText = urllib.parse.quote("참치 마요")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
response_body = response.read()
    print(response_body.decode('utf-8'))
```

```python
import requests
from bs4 import BeautifulSoup

keyword = "디퓨저"
# encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
                        headers={"X-Naver-Client-Id":"CBtyju_UT3NjM1k0Gxk3",
                                "X-Naver-Client-Secret":"lyIS61mwQJ"
                        })

json_obj = result.json()
print(json_obj)
```


## 공공 데이터 포탈 API
### 1. 사이트 접속
- 밑의 url로 접속  
https://www.data.go.kr/

### 2. API 발급
- 사용할 데이터 검색 후 활용 신청 클릭  
![1](https://user-images.githubusercontent.com/32935365/67481179-7af94b80-f69c-11e9-9375-77bcb63c0e89.PNG)

### 3. URL & Query & Sample Code
- [마이페이지]-[오픈API]-[개발계정]-[활용]-[해당 API 선택]-[개발가이드]  
![4](https://user-images.githubusercontent.com/32935365/67481938-d0822800-f69d-11e9-8c0e-eb45e49f4996.PNG)

- Query Parameter, 각 언어별 sample code를 확인 할 수 있음  
![5](https://user-images.githubusercontent.com/32935365/67482021-fc051280-f69d-11e9-8820-c7b18b152388.PNG)
![6](https://user-images.githubusercontent.com/32935365/67482033-032c2080-f69e-11e9-9c06-d57187007eb5.PNG)


### 3. 사용법
```python
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
queryParams = '?'  + 'LAWD_CD=' + '11110' \
                + '&DEAL_YMD=' + '201811' \
                + '&serviceKey=' + 'zxerdxjycZVABMRMsqM6VCZ4d1u4IZPQjZ1QNN%2FGdGSGKTVJ9Z9jEEq9KLbVPTdJBDCqRMG1UGFaCeJM3PezhQ%3D%3D'

url = url + queryParams

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

print(bs_obj)
```

## 정규식
### https://regexr.com/
- 셀트리온. : 셀트리온과 문자(숫자 포함) 하나
- 셀트리온[가-힣] : 셀트리온과 한글 한글자
- 셀트리온[가-힣]{1} : 셀트리온과 한글 1글자
- 셀트리온[가-힣]{3} : 셀트리온과 한글 3글자
- 셀트리온[가-힣]{1,3} : 셀트리온과 한글 1~3글자
- [0-9]{3}-[0-9]{3,4}-[0-9]{4} : 010-1234-5678과 같은 핸드폰 번호
- [0-9]{3}(-|.)[0-9]{3,4}(-|.)[0-9]{4} : 010-1234-5678과 같은 핸드폰 번호와 010 1234 5678과 같은 핸드폰 번호
- 셀트리온[가-힣0-9a-zA-Z]* : 셀트리온으로 시작하는 모든것