import requests
from bs4 import BeautifulSoup

def main():
    url = ""
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content,"html.parser")
    content = bs_obj.find("div",{"class":"content"})
    rprts = content.findAll("div",{"class":"rprt"})

    for item in rprts:
        atag = item.find("a")
        link = "" + atag["href"]
        print(link, atag.text)

        linkResult = requests.get(link)
        subPage = BeautifulSoup(linkResult.content,"html.parser")

        print(subPage.find("div",{"class":"rprt_all"}))

if __name__ == "__main__":
    main()