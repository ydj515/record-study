# -*- encoding: utf-8 -*-
import requests
from urllib.parse import quote

"""
20_naver_api_call_ex.py 참조
"""

def get1000Result(keyword):
    list = []
    for num in range(0, 10):
        list = list + call(keyword, num*100 + 1)['items']
    
    return list

def call(keyword, start):
    encText = quote(keyword)
    print(encText)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start=" + str(start)  # json 결과
    result = requests.get(url=url,
                            headers={"X-Naver-Client-Id":"CBtyju_UT3NjM1k0Gxk3",
                                    "X-Naver-Client-Secret":"lyIS61mwQJ"
                            })
    # result.encoding = 'utf-8'
    json_obj = result.json()
    print(json_obj)

    return json_obj