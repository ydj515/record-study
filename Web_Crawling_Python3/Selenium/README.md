# Selenium

## What is Selenium
- 웹 브라우져를 컨트롤하여 웹 UI 를 Automation 하는 도구 중의 하나
- 원래는 웹 테스트의 자동화를 위해 사용하지만 크롤링도 가능
- Selenium Server와 Selenium Client가 있는데, 로컬 컴퓨터의 웹 브라우져를 컨트롤하기 위해서는 Selenium Client 를 사용 (여기서는 Selenium 3 사용).
- Selenium Client는 WebDriver라는 공통 인터페이스(Common interface)와 각 브라우져 타입별(IE, Chrome, FireFox 등)로 하나씩 있는 Browser Driver로 구성

## Install Selenium

### Selenium Clinet 모듈 설치
```
pip install selenium
```

### 각 Browser별 Selenium 드라이버 설치
- 사용하는 Browser별로 압축파일을 받고 압축 해제
- Chrome : https://sites.google.com/a/chromium.org/chromedriver/downloads
- Firefox : https://github.com/mozilla/geckodriver/releases
- Edge : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Safari : https://webkit.org/blog/6900/webdriver-support-in-safari-10/
- 드라이버 설치 후 드라이버 경로를 **(코드에서)** PATH에 등록
```python
path = "C:/chromedriver_win32/chromedriver.exe"
```

## 코드에서 적용
```python
from selenium import webdriver

# 드라이버 파일 위치
path = "C:/chromedriver_win32/chromedriver.exe"

# selenium으로 제어할 수 있는 브라우저 새창이 뜸
driver = webdriver.Chrome(path)

# driver가 naver 페이지에 접속하도록 명령
driver.get("https://www.naver.com")

# driver를 종료하여 창이 사라진다
# driver.close() # 현재 window를 닫음
driver.quit() # quit()으로 끝내는 것은 완전히 driver를 닫아줌
```

## 함수

### 페이지의 단일 element에 접근하는 api
- driver.find_element_by_name('HTML_name')
- driver.find_element_by_id('HTML_id')
- driver.find_element_by_xpath('/html/body/some/xpath')

### 페이지의 여러 elements에 접근하는 api
- driver.find_element_by_css_selector('#css > div.selector')
- driver.find_element_by_class_name('some_class_name')
- driver.find_element_by_tag_name('h1')

[출처]  
https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html