# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)

    # 현재 페이지가 EUC-KR로 되어 있기 때문에 utf-8로 변환을 먼저 해준다.
    # print(result.encoding)
    result.encoding = 'utf-8'
    
    bs_obj = BeautifulSoup(result.content, "html.parser")

    return bs_obj

def get_candle_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)

    td_first = bs_obj.find("td",{"class":"first"})
    blind = td_first.find("span",{"class":"blind"})

    # close 종가(전일)
    close = blind.text

    # high 고가
    table = bs_obj.find("table",{"class":"no_info"})
    trs = table.findAll("tr")
    first_tr = trs[0]
    first_tr_tds = first_tr.findAll("td")
    first_tr_tds_second_td = first_tr_tds[1]
    high = first_tr_tds_second_td.find("span",{"class":"blind"}).text

    # open 고가
    second_tr = trs[1]
    second_tr_td_first = second_tr.find("td",{"class":"first"})
    blind_open = second_tr_td_first.find("span",{"class":"blind"})
    open = blind_open.text
    
    # low 저가
    second_tr_tds = second_tr.findAll("td")
    second_tr_second_td = second_tr_tds[1]
    blind_low = second_tr_second_td.find("span",{"class":"blind"})
    low = blind_low.text

    # dictionary 형태로 반환
    return {"close":close, "high":high, "open":open, "low":low}

def main():

    # sk 하이닉스 00060, naver035420
    company_codes = ["000660", "035420"]

    for item in company_codes:
        print(get_candle_chart_data(item))
    
if __name__ == "__main__":
    main()