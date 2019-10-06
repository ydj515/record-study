import pandas as pd

pd.set_option('display.max_colwidth', -1)

df = pd.read_json("./naverKeywordResult.json")

# type은 int형임
# 20150522
# print(df['postdate'])

# format에서 %다음 대소문자 구분해야댐!!
# 형식을 datetime type으로 바꿔줌
# 2018-12-08
df['postdate'] = pd.to_datetime(df['postdate'], format="%Y%m%d")
# print(df['postdate'])

# 상위 100개만 추출
df = df.head(100)

# 월 별 filtering
df_jan = df[(df['postdate'] >= "2018-01-01") & (df['postdate'] <= "2018-01-31")]
df_feb = df[(df['postdate'] >= "2018-02-01") & (df['postdate'] <= "2018-02-28")]
df_mar = df[(df['postdate'] >= "2018-03-01") & (df['postdate'] <= "2018-03-31")]
# print(df_jan.count())
# print(df_feb.count())
# print(df_mar.count())

print(df['postdate'].max())
print(df['postdate'].min())

