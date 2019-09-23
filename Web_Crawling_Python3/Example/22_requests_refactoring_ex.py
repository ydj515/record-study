#crawling하는 코드
import requests
from bs4 import BeautifulSoup

# url을 넣어서 bs bs_obj를 return하는 function
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    return bs_obj

# company_code를 받아서 price를 return하는 function
def get_price(company_code):
        
    url = "https://www.naver.com" + company_code
    bs_obj = get_bs_obj(url)
    no_today = bs_obj.find("p",{"class":"no_today"})
    blind = no_today.find("span",{"class":"blind"})

    return blind.text

url = "https://www.naver.com"

price_samsung = get_price("005930")
print(price_samsung)