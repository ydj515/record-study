import pandas as pd
import numpy as np

df = pd.DataFrame({
    'key1':['a','a','b','b','a'],
    'key2':['one','two','one','two','one'],
    'data1':np.random.rand(5),
    'data2':np.random.rand(5)
})



print(df)
#   key1 key2     data1     data2
# 0    a  one  0.501320  0.860983
# 1    a  two  0.674442  0.475954
# 2    b  one  0.268901  0.162381
# 3    b  two  0.821463  0.043981
# 4    a  one  0.315794  0.105666
print("=============================================")

# json 데이터 프레임에 몇개의 데이터가 있는지 추출
print(df.count())
# key1     5
# key2     5
# data1    5
# data2    5
# dtype: int64
print("=============================================")

# 계산할열.groupby(기준이될열)
grouped = df["data1"].groupby(df["key1"])

# 통계함수를 쓰지않아서 값이 나오진 않는다.
print(grouped)
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x067A6250>
print("=============================================")

print(grouped.sum()) # key1의 값인 a, b를 가지고 각 key1이 a일 때 data1의 값을 누적. key1이 b일때 data1의 값을 누적
# key1
# a    1.491556
# b    1.090364
# Name: data1, dtype: float64