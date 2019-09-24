# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
# import sys
# import io
"""
파이썬 크롤러 만들기
Naver 금융 주식 데이터 수집하기
특정 종목의 가격 받아오기
여러 종목의 가격 받아오기
특정 종목의 봉차트 데이터(open, close, high, low) 받아오기
여러 종목의 봉차트 데이터(시고저종) 받아오기
"""
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)

    # 현재 페이지가 EUC-KR로 되어 있기 때문에 utf-8로 변환을 먼저 해준다.
    # print(result.encoding)
    result.encoding = 'utf-8'
    
    bs_obj = BeautifulSoup(result.content, "html.parser")

    return bs_obj

# bs_obj를 받아서 price를 return
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    # print(bs_obj)

    no_today = bs_obj.find("p",{"class":"no_today"})
    # print(no_today)

    blind_now = no_today.find("span",{"class":"blind"})
    # print(blind_now.text)
    return blind_now.text

def main():
    # samsung 005930
    price_samsung = get_price("005930")
    print(price_samsung)

    # hynix 000660
    price_hynix = get_price("000660")
    print(price_hynix)

    print(get_price("005680"))
    
if __name__ == "__main__":
    main()