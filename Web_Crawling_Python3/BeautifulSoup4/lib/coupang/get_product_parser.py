from bs4 import BeautifulSoup

def get_product(li):
    # a = li.find("a",{"class":"baby-product-link"})
    # dl = a.find("dl",{"class":"baby-product-wrap"})
    img = li.find("dt",{"class":"image"}).find("img")
    price_wrap = li.find("div",{"class":"price-wrap"})
    strong = price_wrap.find("strong")
    return {"name":img['alt'], "price":strong.text}

def get_products(string):
    bs_obj = BeautifulSoup(string,"html.parser")
    ul = bs_obj.find("ul",{"id":"productList"})
    lis = ul.findAll("li")
    
    products = []

    for li in lis:
        products.append(get_product(li))

    return products