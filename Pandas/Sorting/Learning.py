import pandas as pd

students = {
    "Name": ["Rohit", "Kabir", "Dev", "Ruda", "Sneha"],
    "Age": [20, 20, 21, 22, 19],
    "Marks": [90, 82, 95, 88, 76]
}

df = pd.DataFrame(students)

print(df.sort_values(by = "Marks"))

print()
print(df.sort_values(by = "Marks", ascending = False))

print()
print(df.sort_values(by = ["Age", "Marks"]))

print()
print(df["Marks"].max())

print()
print(df["Marks"].min())
print(df["Marks"].mean())
print(df["Marks"].sum())
print(df["Marks"].count())

print()
print(df["Age"].unique())
print(df["Marks"].nunique())

