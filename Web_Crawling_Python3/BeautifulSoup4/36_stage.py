# -*- encoding: utf-8 -*-
from lib.naver_api_caller import get1000Result
import json

def main():
    list = []

    result = get1000Result("강남역 맛집")
    result1 = get1000Result("강남역 찻집")

    list = list + result + result1

    a = json.dumps(list) # 리스트를 json형식으로 만들어줌

    file = open("./gangnam.json",'w')
    file.write(a)

    print(len(list))
        
if __name__ == "__main__":
    main()