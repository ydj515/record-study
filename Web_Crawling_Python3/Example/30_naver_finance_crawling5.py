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
    # print(td_first)

    blind = td_first.find("span",{"class":"blind"})

    # close 종가(전일)
    close = blind.text
    # print(close)

    # high 고가
    table = bs_obj.find("table",{"class":"no_info"})
    # print(table)
    
    trs = table.findAll("tr")
    # print(trs)

    first_tr = trs[0]
    first_tr_tds = first_tr.findAll("td")
    # print(first_tr_tds)
    
    first_tr_tds_second_td = first_tr_tds[1]
    print(first_tr_tds_second_td)
    
    high = first_tr_tds_second_td.find("span",{"class":"blind"}).text

    # dictionary 형태로 반환
    return {"close":close, "high":high}

def main():

    # sk하이닉스 000660
    candle_chart_data = get_candle_chart_data("000660")
    print(candle_chart_data)
    
if __name__ == "__main__":
    main()