import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

# url에 해당하는 html이 bsObj에 들어감
bsObj = bs4.BeautifulSoup(html, "html.parser")

# <ul class="an_l">의 ul 태그만 뽑는다
ul = bsObj.find("ul",{"class":"an_l"})

# 위의 찾은 ul 태그에서 li태그를 다 찾아 list 형태로 반환
# [<li></li>, <li></li>, <li></li> ...]
lis = ul.findAll("li")
print(lis)

# 리스트 이므로 길이 출력 가능
print(len(lis))

for li in lis:
    print(li) # 하나씩 꺼내서 출력 하므로 [] 대괄호가 찍히지 않음 cf) 19라인
    
    a_tag = li.find("a")
    span = a_tag.find("span",{"class":"an_txt"})
    
    # .text를 붙히면 안의 값만 나옴
    print(span.text)