from lib.crawler import crawl
from bs4 import BeautifulSoup
from lib.patternMatcher import find_matched_texts

url = "https://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm=%EC%85%80%ED%8A%B8&_=157078184"

page_string = crawl(url)
bs_obj = BeautifulSoup(page_string,"html.parser")


names = find_matched_texts(bs_obj.text, "셀트리온[가-힣0-9a-zA-Z]*")

print(names)

for name in names:
    print(name)