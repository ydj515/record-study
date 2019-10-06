import requests
from bs4 import BeautifulSoup

def get_company_info(code):
    """
    crawling -> 데이터 수집 http request
    종목이름, 가격을 return
    """
    
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    data = requests.get(url)
    bs_obj = BeautifulSoup(data.content, "html.parser")

    wrap_company = bs_obj.find("div",{"class":"wrap_company"})
    print(wrap_company)

    return {"name":"","price":""}