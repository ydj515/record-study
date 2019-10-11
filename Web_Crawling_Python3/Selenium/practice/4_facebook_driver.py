from selenium import webdriver

rootPath = "C:/dev"
driver = webdriver.Chrome(
    executable_path="{}/chromedriver.exe".format(rootPath)
)

url = "https://www.facebook.com/"
driver.get(url) # url로 이동

driver.find_element_by_id("email").send_keys("ydj515@hanmail.net")

# driver.find_element_by_id("pass").send_keys("123456")
driver.find_element_by_xpath("//*[id='pass']").send_keys("123456")

# 로그인버튼의 id 값은 계속 바뀜
driver.find_element_by_id("u_0_b").click() # 로그인 버튼 클릭

driver.close()