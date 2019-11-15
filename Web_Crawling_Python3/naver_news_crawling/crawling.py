#-*- coding:utf-8 -*-
import urllib.request
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_bsobj(url):
    """
    bs_obj를 리턴
    """
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser") # url에 해당하는 html이 bsObj에 들어감

    return bs_obj

def driver_setting():
    pass

def more_news_click(driver):
    """
    뉴스 더보기 클릭
    """
    while True:
        try:
            headline_tag = driver.find_element_by_xpath("//div[@class='cluster_more']/a")
            if headline_tag is not None:
                headline_tag.send_keys('\n')
            else:
                break
        except:
            break

def print_classes(classes):
    """
    debug를 위한 console print
    """
    print("========")
    for i in range(0,len(classes)):
        print(classes[i])
    print("========")

def open_all_new_tabs(classes):
    """
    새탭으로 모두 열기
    """
    for i in range(0,len(classes)):
        print(classes[i])
        classes[i].send_keys(Keys.CONTROL+"\n")
        time.sleep(0.5)

def main():

    driver = webdriver.Chrome("./chromedriver.exe")
    url = "https://news.naver.com/main/main.nhn"
    query = "?mode=LSD&sid1={}"
    all_news = {} # 결과를 담는 dict
    
    # 정치, 경제, 사회, IT, 생활, 세계
    for section in range(100,105):
        # bs_obj = get_bsobj(url + query.format(section))
        
        uri = url + query.format(section)

        if(section==100):
            main_uri = driver.get(uri)

            more_news_click(driver)
            
            classes = driver.find_elements_by_class_name("cluster_foot_more")

            print_classes(classes)

            open_all_new_tabs(classes)

            for i in range(0,len(classes)+1):
                # 제일 마지막 탭부터 1번인듯?
                print(i)
                driver.switch_to_window(driver.window_handles[i])
                current_url_obj = get_bsobj(driver.current_url)
                time.sleep(1)
                
                dls = current_url_obj.findAll("dl")

                for j in range(0,len(dls)):
                    print("==========================")
                    dts = dls[j].findAll("dt") # 0은 i로
                    try: # 뉴스 이미지 있는 것들은 try문에서 크롤링 가능
                        news_url = dts[1].find("a")["href"] # 1은 고정
                        print(news_url)
                        headline = dts[1].find("a").text # 1은 고정
                        print(headline)

                        dd = dls[j].find("dd")

                        news_company = dd.find("span",{"class":"writing"}).text # i로
                        print(news_company)

                        news_date = dd.find("span",{"class":"date"}).text
                        print(news_date)

                        news = get_bsobj(news_url)
                        news_hour = news.find("span",{"class":"t11"}).text

                        print(news_hour)

                        news_content = news.find("div",{"class":"_article_body_contents"}).text
                        print(news_content)

                    except: # 뉴스 이미지 없는 것들은 catch문에서 크롤링
                        news_url = dts[0].find("a")["href"] # 1은 고정
                        print(news_url)
                        headline = dts[0].find("a").text # 1은 고정
                        print(headline)

                        dd = dls[j].find("dd")
                        
                        news_company = dd.find("span",{"class":"writing"}).text # i로
                        print(news_company)

                        news_date = dd.find("span",{"class":"date"}).text
                        print(news_date)

                        news = get_bsobj(news_url)
                        news_hour = news.find("span",{"class":"t11"}).text

                        print(news_hour)

                        news_content = news.find("div",{"class":"_article_body_contents"}).text
                        print(news_content)

                    time.sleep(0.5)

            driver.quit()

        else:
            driver = webdriver.Chrome("./chromedriver.exe")
            main_uri = driver.get(uri)

            more_news_click(driver)
                
            classes = driver.find_elements_by_class_name("cluster_head_more")

            print_classes(classes)

            open_all_new_tabs(classes)

            for i in range(0,len(classes)+1):
                # 제일 마지막 탭부터 1번인듯?
                print(i)
                driver.switch_to_window(driver.window_handles[i])
                current_url_obj = get_bsobj(driver.current_url)
                time.sleep(1)

                dls = current_url_obj.findAll("dl")

                for j in range(0,len(dls)-2):
                    print("==========================")
                    
                    try: # 뉴스 이미지 있는 것들은 try문에서 크롤링 가능
                        dts = dls[j].findAll("dt") # 0은 i로
                        print(dts)
                        news_url = dts[1].find("a")["href"] # 1은 고정
                        print(news_url)
                        headline = dts[1].find("a").text # 1은 고정
                        print(headline)

                        dd = dls[j].find("dd")
                       
                        news_company = dd.find("span",{"class":"writing"}).text # i로
                        print(news_company)

                        news_date = dd.find("span",{"class":"date"}).text
                        print(news_date)

                        news = get_bsobj(news_url)
                        news_hour = news.find("span",{"class":"t11"}).text

                        print(news_hour)

                        news_content = news.find("div",{"class":"_article_body_contents"}).text
                        print(news_content)

                    except: # 뉴스 이미지 없는 것들은 catch문에서 크롤링
                        news_url = dts[0].find("a")["href"] # 1은 고정
                        print(news_url)
                        headline = dts[0].find("a").text # 1은 고정
                        print(headline)

                        dd = dls[j].find("dd")
                        
                        news_company = dd.find("span",{"class":"writing"}).text # i로
                        print(news_company)

                        news_date = dd.find("span",{"class":"date"}).text
                        print(news_date)

                        news = get_bsobj(news_url)
                        news_hour = news.find("span",{"class":"t11"}).text

                        print(news_hour)

                        news_content = news.find("div",{"class":"_article_body_contents"}).text
                        print(news_content)

                    time.sleep(0.5)

    print(all_news)
    
if __name__ == "__main__":
    main()