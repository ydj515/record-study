
import requests
from urllib.parse import urlparse



keyword = "디퓨저"
# encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
                        headers={"X-Naver-Client-Id":"CBtyju_UT3NjM1k0Gxk3",
                                "X-Naver-Client-Secret":"lyIS61mwQJ"
                        })

json_obj = result.json()
print(json_obj)
