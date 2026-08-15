import pandas as pd

employees = {
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rohit", "Kabir", "Dev", "Ruda", "Sneha", "Aman"],
    "Department": ["AI", "HR", "AI", "Sales", "HR", "AI"],
    "Salary": [60000, 45000, 72000, 50000, 48000, 68000],
    "Experience": [2, 1, 3, 2, 1, 4]
}

df = pd.DataFrame(employees)

print("Dimensions of Dataframe: \n", df.shape)
print("\nName of Columns: \n", df.columns)

print("\nName & Salary Column: \n", df[["Name", "Salary"]])

print("\nSalary greater than 50,000: \n", df[df["Salary"] > 50000])
print("\nSalary greater than 60,000 & Experience greater than 2years: \n", df[ (df["Salary"] > 60000) & (df["Experience"] > 2)])

print("\nName: \n", df.loc[:, "Name"])
print("\nDepartment: \n", df.loc[:, "Department"])