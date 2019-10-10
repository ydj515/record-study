import requests

def crawl(keyword, page_no):
    # all.nhn?query=숨셔바요 & & &
    # all.nhn?query=에어컨 & & &
    # all.nhn?query=가습기 & & &
    url = "https://search.shopping.naver.com/search/all.nhn?origQuery={}&pagingIndex={}&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query={}".format(keyword,page_no,keyword)
    data = requests.get(url)
    # print(data.status_code, url)
    return data.content