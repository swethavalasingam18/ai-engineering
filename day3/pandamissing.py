# %%   ← this line says "new cell starts here"
import pandas as pd
import numpy as np

data = {
    'name': ['Amit', 'Priya', 'Amit', 'Ravi', 'Sneha', None, 'Ravi'],
    'age': [25, 30, 25, np.nan, 28, 35, 40],
    'city': ['Hyderabad', 'Pune', 'Hyderabad', 'Delhi', None, 'Mumbai', 'Delhi'],
    'salary': [45000, 60000, 45000, 55000, 50000, 70000, 55000]
}
df = pd.DataFrame(data)
print(df)

# %%  ← this line says "new cell starts here"
print(df.isna().sum())

# %%
df['age'] = df['age'].fillna(0)
df['name'] = df['name'].fillna('Unknown')
df['city'] = df['city'].fillna('Unknown')
print(df)
# %%
print (df.duplicated().sum())

# %%
df = df.drop_duplicates()
print(df)

# %% value and counts how many rows fall in each city.
print(df.groupby('city').size())

# %% it adds up the salary values within each city group.
print(df.groupby('city')['salary'].sum())

# %% picks the highest salary in each city.
print(df.groupby('city')['salary'].max())

# %% salary, lowest to highest (ascending is the default).
print(df.sort_values('salary'))
# %% Same column, but highest to lowest.
print(df.sort_values('salary', ascending=False))
# %% cities alphabetically (A→Z), and within each city, 
# salary from highest to lowest.
print(df.sort_values(['city', 'salary'], ascending=[True, False]))