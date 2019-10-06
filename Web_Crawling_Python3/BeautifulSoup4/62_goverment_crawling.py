import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl(url):
    data = requests.get(url)
    # print(data, url)

    return data.content

def parser(page_string):
    bs_obj = BeautifulSoup(page_string, "html.parser")

    table = bs_obj.find("table", {"class":"table table-striped2"})
    # print(table)
    tbody = table.find("tbody")
    trs = tbody.findAll("tr")

    product_infos = []
    for tr in trs:
        product_info =  get_product_info(tr)
        # print(product_info)
        product_infos.append(product_info)

   
    return product_infos

def get_product_info(tr):
    # print(tr)
    tds = tr.findAll("td")
    # print(tds)

    return {"no":tds[0].text,"name":tds[1].text, "category":tds[2].text, "vendor":tds[3].text, "confirmNo":tds[4].text, "licenseNo":tds[5].text}

def crawl_page(page_no):
    url = "http://ecolife.me.go.kr/ecolife/sntryAid/index?page={}".format(page_no)

    page_string = crawl(url)
    products = parser(page_string)

    return products

def save_file(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer,'Sheet1')
    writer.save()

def main():

    result = []
    
    for page_no in range(1,164 + 1): # 165 page까지
        result = result + crawl_page(page_no)
    
    # print(result)
    # print(len(result))

    df = pd.DataFrame(data=result)
    save_file(df, "./ecolife.xlsx")

if __name__ == "__main__":
    main()