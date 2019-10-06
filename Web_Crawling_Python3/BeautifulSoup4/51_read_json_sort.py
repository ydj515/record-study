import pandas as pd

pd.set_option('display.max_colwidth', -1)

# [[],[],[],[]]
df = pd.read_json("./195297.json")

# df 내용
print(df)

# df의 갯수
print(df.count())

# print(df.head(10)) # 상위 10개
print(df[['name','price']].head(10)) # 상위 10개의 name, price만
print(df[['name','price' ]].tail(10)) # 하위 10개의 name, price만

# 오름차순으로 sort
df_sorted = df.sort_values(['price'])
print(df_sorted)

# 내림차순으로 sort
df_sorted_ascending = df.sort_values(['price'], ascending=[0])
print(df_sorted_ascending)

# 상위 5개 출력
print(df_sorted_ascending.head(5))

