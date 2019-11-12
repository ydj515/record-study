#-*- coding:utf-8 -*-
import urllib.request
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_bsobj(url):

    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser") # url에 해당하는 html이 bsObj에 들어감

    return bs_obj

def main():

    driver = webdriver.Chrome("./chromedriver.exe")

    url = "https://news.naver.com/main/main.nhn"
    query = "?mode=LSD&sid1={}"

    all_news = {}
    
    # 정치, 경제, 사회, IT, 생활, 세계
    for section in range(100,105):
        # bs_obj = get_bsobj(url + query.format(section))
        
        uri = url + query.format(section)

        if(section==100):
            main_uri = driver.get(uri)

           
            while True:
                try:
                    headline_tag = driver.find_element_by_xpath("//div[@class='cluster_more']/a")
                    if headline_tag is not None:
                        headline_tag.send_keys('\n')
                    else:
                        break
                except:
                    break
            

            classes = driver.find_elements_by_class_name("cluster_foot_more")

            print("========")
            for i in range(0,len(classes)):
                print(classes[i])
            print("========")

            # 새 탭으로 모두 열기
            for i in range(0,len(classes)):
                print(classes[i])
                classes[i].send_keys(Keys.CONTROL+"\n")
                time.sleep(0.5)
            

            for i in range(0,len(classes)+1):
                # 제일 마지막 탭부터 1번인듯?
                print(i)
                driver.switch_to_window(driver.window_handles[i])
                current_url_obj = get_bsobj(driver.current_url)
                time.sleep(1)
                # td_content = current_url_obj.find("td",{"class":"content"})
                dts = current_url_obj.findAll("dt",{"class":"photo"})
                # print(len(dts))
                a_tags = []

                # 모든 탭 url 모으기
                for j in range(0,len(dts)):
                    a_tag = dts[j].find("a")["href"]
                    print(a_tag)
                    a_tags.append(a_tag)

                all_news[str(section)+str(i)] = a_tags # 모든 뉴스 딕셔너리에 담기
                print("==========================")
                time.sleep(0.5)

            # print(len(driver.window_handles)+1)
            # for j in range(1,len(driver.window_handles)+1):
                # print(j)
                # driver.switch_to_window(driver.window_handles[len(classes)+1 - j])
                # time.sleep(1)
            driver.quit()

        else:
            driver = webdriver.Chrome("./chromedriver.exe")
            main_uri = driver.get(uri)

            while True:
                try:
                    headline_tag = driver.find_element_by_xpath("//div[@class='cluster_more']/a")
                    if headline_tag is not None:
                        headline_tag.send_keys('\n')
                    else:
                        break
                except:
                    break
                
            classes = driver.find_elements_by_class_name("cluster_head_more")

            print("========")
            for i in range(0,len(classes)):
                print(classes[i])
            print("========")

            # 새 탭으로 모두 열기
            for i in range(0,len(classes)):
                print(classes[i])
                classes[i].send_keys(Keys.CONTROL+"\n")
                time.sleep(0.5)
            

            for i in range(0,len(classes)):
                # 제일 마지막 탭부터 1번인듯?
                print(i)
                driver.switch_to_window(driver.window_handles[i])
                current_url_obj = get_bsobj(driver.current_url)
                time.sleep(2)
                # td_content = current_url_obj.find("td",{"class":"content"})
                dts = current_url_obj.findAll("dt",{"class":"photo"})
                # print(len(dts))
                a_tags = []

                # 모든 탭 url 모으기
                for j in range(0,len(dts)):
                    a_tag = dts[j].find("a")["href"]
                    print(a_tag)
                    a_tags.append(a_tag)

                all_news[str(section)+str(i)] = a_tags # 모든 뉴스 딕셔너리에 담기
                print("==========================")
                time.sleep(0.5)


    print(all_news)
    
if __name__ == "__main__":
    main()