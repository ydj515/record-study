from selenium import webdriver
from time import sleep

rootPath = "C:/chromedriver_win32"

driver = webdriver.Chrome(
    executable_path="{}/chromedriver.exe".format(rootPath)
)

url = "http://dart.fss.or.kr/"

driver.get(url)

driver.find_element_by_id("textCrpNm").send_keys("셀트리온")
driver.find_element_by_xpath("//*[@id='searchForm']/fieldset/p[4]/input").click()

sleep(5)
print("==== 5sec end ====")

driver.find_element_by_xpath("//*[@id='checkCorpSelect']").click()
driver.find_element_by_xpath("//*[@id='corpListContents']/div/fieldset/div[3]/a[1]/img").click()


driver.find_element_by_xpath("//*[@id='searchpng']").click()

page_string = driver.page_source
print(page_string)

sleep(5)
print("==== 5sec end ====")

driver.quit()