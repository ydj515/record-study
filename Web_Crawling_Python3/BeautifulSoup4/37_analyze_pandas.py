import pandas as pd

def main():

    # json 데이터 읽기
    df = pd.read_json("./gangnam.json")

    # json 데이터 프레임에 몇개의 데이터가 있는지 추출
    print(df.count())
    # title          2000
    # link           2000
    # description    2000
    # bloggername    2000
    # bloggerlink    2000
    # postdate       2000
    print("=============================================")

    # 계산할열.groupby(기준이될열)
    # 중복 제거해서 보여줌
    dfSum = df.groupby('bloggername').sum()
    print(dfSum)
    # title                                               link  ...                         bloggerlink  postdate
    # bloggername                                                                                                                  ...
    # "日本満喫‼"블러그                                                       블루보틀 커피  https://blog.naver.com/magicsoup79?Redirect=Lo...  ...  https://blog.naver.com/magicsoup79  20180401
    # "돌콩's SCRIGNO"                 <b>강남역 맛집</b> 로리스더프라임립 스테이크와는 또 다른 매력...   https://blog.naver.com/tonyny35?Redirect=Log&l...  ...     https://blog.naver.com/tonyny35  20190802
    # "언제나 감사하며 살자"                                                   조촐한 아침식사  https://blog.naver.com/gaesun?Redirect=Log&log...  ...       https://blog.naver.com/gaesun  20180106
    # "영어대장" 국내, 해외의 영어교육 정보를 생생하게!         [<b>강남역 맛집</b>] 함박스테이크와 카레는 요기다~!!  https://blog.naver.com/timesmedia?Redirect=Log...  ...   https://blog.naver.com/timesmedia  20190824
    # "해강+재곰=해곰이"  
    print("=============================================")
    
    # 제목을 기준으로 blogger name 출력
    bloggernames = df['title'].groupby(df['bloggername']).sum()
    print(bloggernames)
    # bloggername
    # "日本満喫‼"블러그                                                         블루보틀 커피
    # "돌콩's SCRIGNO"                   <b>강남역 맛집</b> 로리스더프라임립 스테이크와는 또 다른 매력...
    # "언제나 감사하며 살자"                                                     조촐한 아침식사
    # "영어대장" 국내, 해외의 영어교육 정보를 생생하게!           [<b>강남역 맛집</b>] 함박스테이크와 카레는 요기다~!!
    # "해강+재곰=해곰이"                                            그동안 내가 살이 1도 안빠진 이유
    print("=============================================")

if __name__ == "__main__":
    main()