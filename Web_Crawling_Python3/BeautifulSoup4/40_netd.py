import requests
from bs4 import BeautifulSoup

url = "http://www.netd.ac.za/?action=browse&category=Affiliation&order=asc"

result = requests.get(url)

bs_obj = BeautifulSoup(result.content, "html.parser")

# view&identifier=oai%3Aunion.ndltd.org%3Acput%2Foai%3Alocalhost%3A20.500.11838%2F727

ol = bs_obj.find("ol",{"start":"1"})
# print(ol)

lis = ol.findAll("li")
for li in lis:
    print("http://www.netd.ac.za/" + li.find("a")["href"])