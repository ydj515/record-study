import requests
from bs4 import BeautifulSoup

# 각 페이지 마다 start부분의 값만 바뀐다
def getLinks(start):
    url = "http://www.netd.ac.za/portal/?action=browse&category=Affiliation&maxresults=10&start=" +str(start) +"&order=asc"
    result = requests.get(url)

    bs_obj = BeautifulSoup(result.content, "html.parser")

    # view&identifier=oai%3Aunion.ndltd.org%3Acput%2Foai%3Alocalhost%3A20.500.11838%2F727

    ol = bs_obj.find("ol")
    # print(ol)

    links = []
    lis = ol.findAll("li")

    for li in lis:
        link = "http://www.netd.ac.za/" + li.find("a")["href"]
        links.append(link)
        # print(link)

    return links