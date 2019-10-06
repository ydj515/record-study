from lib.string_getter import get_page_string
from lib.coupang.get_product_parser import get_products

category_products = []


for page_num in range(1,18): # 1 ~ 17
    url = "https://www.coupang.com/np/categories/186764?page={}".format(page_num)

    page_string = get_page_string(url)
    products = get_products(page_string)

    category_products = category_products + products

# 60 * 17(한페이지당 60개잇음)
print(len(category_products))

for product in category_products:
    print(product)