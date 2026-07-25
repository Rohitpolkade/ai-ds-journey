import pandas as pd

employees = {
    "Name": ["Rohit", "Kabir", "Dev", "Ruda", "Sneha", "Aman"],
    "Department": ["AI", "HR", "AI", "Sales", "HR", "AI"],
    "Salary": [60000, 45000, 72000, 50000, 48000, 68000],
    "Experience": [2, 1, 3, 2, 1, 4]
}

df = pd.DataFrame(employees)

print("=" * 50)
print("DEPARTMENT SALARY ANALYZER")
print("=" * 50)

print("\nOriginal DataFrame: ")
print(df)

print("\nAverage Salary: ")
print(df.groupby("Department")["Salary"].mean())

print("\nHighest Salary: ")
print(df.groupby("Department")["Salary"].max())

print("\nLowest Salary: ")
print(df.groupby("Department")["Salary"].min())

print("\nTotal Salary: ")
print(df.groupby("Department")["Salary"].sum())

print("\nEmployee Count: ")
print(df.groupby("Department")["Name"].count())

summary = df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum", "count"])
print("\nDepartment Salary Summary: ")
print(summary)