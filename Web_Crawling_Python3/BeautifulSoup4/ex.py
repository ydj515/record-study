import requests
from bs4 import BeautifulSoup
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

html = '''
<html> 
    <head> 
    </head> 
    <body> 
        <h1> 시장  
            <p id='fruits1' class='name' title='바나나'> 바나나 
                <span class = 'price'> 3000원 </span> 
                <span class = 'inventory'> 500개 </span> 
                <span class = 'store'> 가가가 </span> 
                <a href='http://test1'> url1 </a> 
            </p> 

            <p id='fruits2' class='name' title='귤'> 귤 
                <span class = 'price'> 2000원 </span> 
                <span class = 'inventory'> 100개 </span> 
                <span class = 'store'> 나나나</span> 
                <a href='http://test2'> url2 </a> 
            </p> 
            <p id='fruits3' class='name' title='파인애플'> 파인애플 
                <span class = 'price'> 5000원 </span> 
                <span class = 'inventory'> 10개 </span> 
                <span class = 'store'> 가가가</span> 
                <a href='http://test1' class='my'> url1 </a> 
            </p>
            <div> </div>
        </h1> 
    </body> 
</html>
'''
soup = BeautifulSoup(html, 'html.parser')  
my = soup.select('a')


print(my[0]['href'])

# data = {}

# for title in my_titles:
#     data[title.text] = title.get('href')

# with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#     json.dump(data, json_file)
