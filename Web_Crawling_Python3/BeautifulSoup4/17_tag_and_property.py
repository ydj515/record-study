import bs4

# tag               태그    <ul> <li> <div> ...
# property          속성    class, id, href, title. src
# property value    속성값  class="greet">에서 greet이 속성값
# <a href="www.naver.com"> 여기선 tag : a, property : href, property value : www.naver.com

# string에 따옴표(")를 세개를 쓰면 여러줄로 쓸 수 있음. 아니면  역슬래시(\)를 붙혀야함
# EX)
# html = "<html>" \
#           <body></body> \
#         </html>

def main():
    html = """
    <html>
        <body>
            <ul class="greet">
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>
            </ul>

            <ul class="reply">
                <li>ok</li>
                <li>no</li>
                <li>sure</li>
            </ul>
        </body>
    </html>
    """

    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    ul_reply = bs_obj.find("ul", {"class":"reply"})
    print(ul_reply)

    lis = ul_reply.findAll("li")

    for li in lis:
        print(li.text)
    
if __name__ == "__main__":
    main()