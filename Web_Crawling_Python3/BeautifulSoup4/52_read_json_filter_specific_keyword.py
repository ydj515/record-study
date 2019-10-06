import pandas as pd
import math
pd.set_option('display.max_colwidth', -1)

# [[],[],[],[]]
df = pd.read_json("./195297.json")

# df_filtered = df[df['price'] <= 1000]
# print(df_filtered)

# print(df['name'].head(100))

keywords = ["페레로로쉐", "킨더", "트윅스", "엠앤엠"]

print("total",df['name'].count())
total_count = df['name'].count()

for keyword in keywords:
    df_filtered = df[df['name'].str.contains(keyword)]
    # print(df_filtered['name'].head(10))
    count = df_filtered['name'].count()
    print(keyword, count, str(math.floor(count/total_count*100)) + "%")
