import lib.crawler as crawler
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
str = crawler.crawl(url)

print(str)