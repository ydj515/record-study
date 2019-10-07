import pandas as pd

df = pd.read_json("./products.json")

print(df.count())

writer = pd.ExcelWriter("products.xlsx")
df.to_excel(writer,"sheet1")
writer.save()