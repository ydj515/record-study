from lib.crawl import crawl
from lib.parser import parse
import json
import pandas as pd

json_file_name = "./products.json"

def write_json(json_file_name, total_products):
    file = open("./products.json","w+")
    file.write(json.dumps(total_products))

def write_excel(json_file_name):
    df = pd.read_json("./products.json")

    print(df.count())

    writer = pd.ExcelWriter("products.xlsx")
    df.to_excel(writer,"sheet1")
    writer.save()

def main():

    total_products = []

    shopping_list = ['텀블러','가습기','숨셔바요','텀블러']

    for no in range(0,4):
        for page_no in range(2, 5):
            page_string = crawl(shopping_list[no],page_no)
            products = parse(page_string) # []
            total_products += products
        print("--------------------------------------------")

    for product in total_products:
        print(product)

    write_json(json_file_name, total_products)

    write_excel(json_file_name)
    

if __name__ == "__main__":
    main()