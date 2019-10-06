import pandas as pd

pd.set_option('display.max_colwidth', -1)

df = pd.read_json("./naverKeywordResult.json")

# print(df.count())

# 상위 10개 블로거 이름
df_top5 = df.head(5)
# print(df_top5['bloggername'])

df_filtered = df[df['bloggername'] == 'qazulic님의 블로그']
# print(df_filtered.count())
# print(df_filtered['bloggername'])
# print(df_filtered['link'][0])
print(df_filtered['link'][0].replace("amp;","")) # link 주소에서 amp;를 제거