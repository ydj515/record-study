import requests

url = "http://jolse.com/category/antiaging/53/"

result = requests.get(url)
print(result) # 200 OK