import pandas as pd
import numpy as np

students = {
    "Name": ["Rohit", "Kabir", "Dev", "Ruda", "Sneha"],
    "Age": [20, np.nan, 21, 22, np.nan],
    "Marks": [90, 82, np.nan, 88, 76]
}

df = pd.DataFrame(students)

print("=" * 50)
print("STUDENT DATA CLEANER")
print("=" * 50)

print("\nOriginal DataFrame: ")
print(df)

print("\nMissing Values: \n", df.isnull())

print("\nMissing Count: \n", df.isnull().sum())

clean_df = df.dropna()
print("\nRows without Missing Data: \n", clean_df)

print()
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nFilled DataFrame: \n", df)
