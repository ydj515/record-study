import bs4

# string에 따옴표(")를 세개를 쓰면 여러줄로 쓸 수 있음. 아니면  역슬래시(\)를 붙혀야함
# EX)
# html = "<html>" \
#           <body></body> \
#         </html>
html = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>

        <ul class="replay">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html, "html.parser")

# ul이 여러개지만 find로 찾을 경우는 첫번째 ul만 나옴
ul = bs_obj.find("ul")

print(ul)
print(ul.text)

lis = bs_obj.findAll("li")
print(lis)
print(type(lis)) # <class 'bs4.element.ResultSet'>
print(type(lis[0])) # <class 'bs4.element.Tag'>
print(lis[1].text)

for li in lis:
    print(li)

print("=====================")

for li in lis[1:2]: # for(int i=1; i<2; i++)
    print(li) # <li>bye</li>