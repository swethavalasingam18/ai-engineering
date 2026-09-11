import pandas as pd

df = pd.read_csv('C:/Users/SWITHIN/Documents/ai-engineering/day2/employees.csv')
#print(df.head())
print(df[df["Experience"] > 5])
if len(df[df["Department"] == "IT"]) > 0:
        print("IT employees exist")
print(df[df["Department"] == "Finance"] [["Name" , "Department"]])

print(df[(df["Department"] == "IT") & (df["Experience"] > 8)])

 