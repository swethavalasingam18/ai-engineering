# %%
import pandas as pd
import numpy as np

# Simulated e-commerce order data
data = {
    'order_value': [450, 500, 480, 520, 470, 510, 490, 15000, 460, 505],
    'delivery_days': [2, 3, 2, 4, 3, 2, 3, 5, 2, 3],
    'customer_age': [25, 34, 29, 45, 31, 28, 38, 50, 26, 33]
}
df = pd.DataFrame(data)
print(df)

# %%
print("Mean order value:", df['order_value'].mean())
print("Median order value:", df['order_value'].median())
print("Std dev order value:", df['order_value'].std())

# %%
print(df['order_value'].hist(bins=10))

print (df.corr())

# %%
df_no_outlier = df[df['order_value'] < 1000]  # drops the 15000 row
print(df_no_outlier.corr())