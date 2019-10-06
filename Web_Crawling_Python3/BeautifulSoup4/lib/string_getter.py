import requests

def get_page_string(url):

    data = requests.get(url)
    print(data.status_code) # 200
    return data.content