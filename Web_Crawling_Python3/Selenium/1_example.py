from selenium import webdriver

# 드라이버 파일 위치
path = "C:/dev/chromedriver.exe"

# selenium으로 제어할 수 있는 브라우저 새창이 뜸
driver = webdriver.Chrome(path)

# driver가 naver 페이지에 접속하도록 명령
driver.get("https://www.naver.com")

# driver를 종료하여 창이 사라진다
driver.quit()