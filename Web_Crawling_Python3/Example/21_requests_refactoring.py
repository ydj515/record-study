#crawling하는 코드
import requests
from bs4 import BeautifulSoup

# url을 넣어서 bs bs_obj를 return하는 function
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    return bs_obj

url = "https://www.naver.com"
bs_obj = get_bs_obj(url)
print(bs_obj)

# url = "https://www.naver.com"
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
# bs_obj = get_bs_obj(url)
# print(bs_obj)