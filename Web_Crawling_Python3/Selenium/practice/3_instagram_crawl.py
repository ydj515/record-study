from lib.crawler import crawl
from selenium import webdriver
from time import sleep

"""
인스타 그램은 해시 태그 때문에 셀레니움으로 하는게 편함
"""

url = "https://www.instagram.com/?hl=ko"

page_string = crawl(url)
print(page_string)

rootPath = "C:/dev"
driver = webdriver.Chrome(
    executable_path="{}/chromedriver.exe".format(rootPath)
)

url = "https://instagram.com/explore/tags/발레"
print(url)
driver.get(url) # 엔터를 치는 것

sleep(5)

page_string = driver.page_source
print(page_string)

# 인스타 내용 <div class="Nnq7Caaa"

driver.close()