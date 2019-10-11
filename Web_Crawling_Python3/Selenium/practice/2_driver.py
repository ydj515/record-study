from selenium import webdriver

rootPath = "C:/chromedriver_win32"

driver = webdriver.Chrome(
    executable_path="{}/chromedriver.exe".format(rootPath)
)

url = "https://instagram.com/explore/tags/발레"
print(url)
driver.get(url) # 엔터를 치는 것

page_string = driver.page_source

print(page_string)

driver.quit()