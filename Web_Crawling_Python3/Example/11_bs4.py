import bs4

def main():
    html_str = "<html><div></dib></html>"

    # html_str에 해당하는 html이 bsObj에 들어감
    bsObj = bs4.BeautifulSoup(html_str, "html.parser")

    print(type(bsObj))
    print(bsObj)

    # div 태그를 찾아줌
    print(bsObj.find("div"))
    
if __name__ == "__main__":
    main()