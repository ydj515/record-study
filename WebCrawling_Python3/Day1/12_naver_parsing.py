import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

# url에 해당하는 html이 bsObj에 들어감
bsObj = bs4.BeautifulSoup(html, "html.parser")

# url의 html코드를 그대로 읽어 온다
print(html.read()) # 들여쓰기 안해줌
print(bsObj) # 들여쓰기 해줌

# <div class="area_links">의 div 태그만 뽑아줌
example = bsObj.find("div", {"class":"area_links"})
print(example)

# example의 div안에 있는 a 태그 뽑아줌
example2 = example.find("a")
print(example2)

# .text : example의 div안에 있는 a 태그안에 있는 값만 뽑아줌
print(example2.text)