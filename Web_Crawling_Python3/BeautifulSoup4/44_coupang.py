from lib.string_getter import get_page_string
from lib.coupang.get_product_parser import get_products

def main():
    url = "https://www.coupang.com/np/categories/186764"
    # https://www.coupang.com/np/categories/186764?page=2

    page_string = get_page_string(url)
    products = get_products(page_string)

    for product in products:
        print(product)

if __name__ == "__main__":
    main()