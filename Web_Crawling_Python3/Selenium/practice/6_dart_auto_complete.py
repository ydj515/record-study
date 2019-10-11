from lib.crawler import crawl
from bs4 import BeautifulSoup

url="https://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm=%EC%85%80%ED%8A%B8&_=157078184"

page_string = crawl(url)

bs_obj = BeautifulSoup(page_string,"html.parser")

print(bs_obj)