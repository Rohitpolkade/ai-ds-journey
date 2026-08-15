import pandas as pd
import numpy as np

students = {
    "Name" : ["Rohit", "kabir", "Dev"],
    "Age" : [20, np.nan, 19],
    "Marks" : [90, 91, np.nan]
}

df = pd.DataFrame(students)

print(df)

print()
print(df.isnull())

print()
print(df.isnull().sum())

print()
print(df.notnull())

clean_df = df.dropna()
print()
print(clean_df)

print()
df["Age"] = df["Age"].fillna(21)
print(df)

