from bs4 import BeautifulSoup

def main():
    html = """
    <html>
        <table>
            <tr>
                <td class="first">100</td>
                <td>200</td>
            </tr>
            <tr>
                <td>300</td>
                <td>400</td>
            </tr>

    </html>
"""

    bs_obj = BeautifulSoup(html, "html_parser")
    # print(bs_obj)

    # 100
    td_first = bs_obj.find("td",{"class":"first"})
    # print(td_first)

    # 200
    table = bs_obj.find("table")
    # print(table)
    tr = table.find("tr")
    # print(tr)
    tds = tr.findAll("td")
    print(tds)
    print(tds[1].text)

    # 300
    trs = table.findAll("tr")
    second_tr = trs[1]
    print(second_tr)

    td_300 = second_tr.find("td")
    print(td_300.text)

    # 400
    second_tr_tds = second_tr.findAll("td")
    print(second_tr_tds)
    td_400 = second_tr_tds[1]
    print(td_400.text)
        
if __name__ == "__main__":
    main()