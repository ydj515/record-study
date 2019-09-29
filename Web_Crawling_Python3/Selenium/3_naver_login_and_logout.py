from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
# selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("C:/dev/chromedriver.exe")
 
# "naver login"에 접속한다
# driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
driver.get("https://www.naver.com")


# 아이디 치는 html 태그에 접근한다
element = driver.find_element_by_class_name("lg_local_btn")

# 네이버 로그인 클릭
clik_login_element = element.click()

# 로그인 클릭 후 id 찾기
input_id = driver.find_element_by_id("id")

# 아이디 치는 태그에 아이디를 입력
input_id.send_keys("ydj515")

# tab키 침
# driver.send_keys(Keys.TAB)

# password를 친다
input_pw = driver.find_element_by_id("pw")
input_pw.send_keys("elwpdl515")

click_login = driver.find_element_by_class_name("btn_global")

# 3초 대기
time.sleep(3)

# 로그인 버튼 클릭
click_login.click()

# 로그아웃 버튼 클릭
log_out = driver.find_element_by_class_name("btn_logout")
log_out.click()

# driver를 종료하여 창이 사라진다
driver.quit()