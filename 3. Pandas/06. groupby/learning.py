import pandas as pd

students = {
    "Name": ["Rohit", "Kabir", "Dev", "Ruda", "Sneha", "Aman"],
    "Department": ["AI", "AI", "CSE", "AI", "CSE", "AI"],
    "Marks": [90, 82, 95, 88, 76, 91],
    "Age": [20, 20, 21, 22, 19, 21]
}

df = pd.DataFrame(students)

# This only creates groups but doesn't useful result
df.groupby("Department")

print(df.groupby("Department")["Marks"].mean())

print()
print(df.groupby("Department")["Marks"].max())

print()
print(df.groupby("Department")["Marks"].min())

print()
print(df.groupby("Department")["Name"].count())

print()
print(df.groupby("Department")["Marks"].agg(["mean", "max", "min", "sum", "count"]))

