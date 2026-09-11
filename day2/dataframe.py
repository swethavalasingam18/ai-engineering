import pandas as pd 

students = {
    "Name": ["Sneha", "Karan", "Divya"],
    "Marks": [88, 76, 95],
    "Subject": ["Math", "Science", "English"]
}

df = pd.DataFrame(students)
print(df)
print(df["Marks"])
print(df.shape)