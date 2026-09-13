# %%
import numpy as np
import pandas as pd

np.random.seed(42)  # keeps results reproducible so we see the same numbers

n = 100
order_value = np.random.normal(500, 100, n)      # random orders around ₹500
delivery_days = np.random.randint(1, 6, n)        # random delivery days, 1-5
customer_age = np.random.randint(20, 60, n)       # random ages, 20-60

df_big = pd.DataFrame({
    'order_value': order_value,
    'delivery_days': delivery_days,
    'customer_age': customer_age
})

print(df_big.describe())

# %%
print(df_big.corr())

# %%
# order_value_with_bonus increases when delivery is faster (real business logic: 
# express delivery orders tend to be bigger/rushed purchases)
df_big['order_value_v2'] = df_big['order_value'] + (6 - df_big['delivery_days']) * 50

print(df_big[['order_value_v2', 'delivery_days']].corr())