import requests
from bs4 import BeautifulSoup

def crawl(url):
    result = requests.get(url)
    result.encoding = 'utf-8'

    bs_obj = BeautifulSoup(result.content,"html.parser")
    return bs_obj