import pandas as pd

fruits_price = [40, 60, 30]
print(fruits_price)

lables=["Apple", "Banana", "Mango"]
series_lable=pd.Series(fruits_price , index = lables)
print(series_lable)

print("Price of Banana:", series_lable["Banana"])