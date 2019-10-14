from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup


rootPath = "C:/chromedriver_win32"

driver = webdriver.Chrome(
    executable_path="{}/chromedriver.exe".format(rootPath)
)

url = "https://pythonclock.org/"

driver.get(url)

sleep(2)
page_string = driver.page_source
print(type(page_string))

a = page_string.find("python-27-clock is-countdown")

print(a)

# python-27-clock is-countdown
sleep(2)




driver.quit()