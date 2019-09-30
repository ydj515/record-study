import pandas as pd

df = pd.read_json("./gangnam.json")
print(df.count())

# 가장많이 등장하는 블로그 이름
# dfSum = df.groupby('bloggername').sum()
# print(dfSum)

# 블로그 이름만 출력
bloggernames = df['bloggername'].groupby()
print(bloggernames)