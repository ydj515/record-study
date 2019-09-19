from urllib.request import urlopen
import bs4

url = "http://news.naver.com/"
# import urllib.request만 할 경우
# html = urllib.request.urlopen(url)
html = urlopen(url)
# print(html.read())

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")
# print(bs_obj)

div = bs_obj.find("div",{"id":"main_content"})
divs = div.findAll("div")

for div in divs:
    strong = div.find("strong")
    if strong is not None: # strong 태그가 없는 div에는 None이 출력되어서 조건문 추가
        # print(strong)
        print(strong.text)

# 16~20라인까지의 결과를 리스트에 저장. 여기에 none이 들어 갈 수 없기때문에 여기선 오류
titles = [div.find("strong").text for div in divs]
print(titles)