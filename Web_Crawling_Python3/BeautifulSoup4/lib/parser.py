from bs4 import BeautifulSoup

def get_product_info(li):
    
    # print(li)

    img = li.find("img")
    alt = img['alt'] # alt 속성
    price_reload = li.find("span", {"class":"_price_reload"})
    
    if(price_reload==None): # 네이버 쇼핑 페이지 가보면 최저 ~~원 인 것은 class가 _price_reload이고, 그냥 가격만 써있으면 class가 num이다
        price_reload = li.find("span", {"class":"num"})


    print(price_reload)
    a_link = li.find("a",{"class":"link"})
    href = a_link['href']

    # print(href)

    return {"name":alt, "price":price_reload.text, "link":href}
    # return {"name":alt, "price":price_reload.text.replace(",",""), "link":href} # 17,300 -> 17300으로 replace해줌

def parse(page_string):

    bs_obj = BeautifulSoup(page_string, "html.parser")

    ul = bs_obj.find("ul",{"class":"goods_list"})
    lis = ul.findAll("li",{"class":"_itemSection"})

    products = []

    for li in lis:
        product = get_product_info(li)
        products.append(product)

    return products