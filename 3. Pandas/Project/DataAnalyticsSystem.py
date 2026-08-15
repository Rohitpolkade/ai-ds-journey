import pandas as pd
import numpy as np

employees = {
    "ID": [101,102,103,104,105,106,107,108],
    "Name": [
        " rohit ",
        "KABIR",
        "dev",
        "RuDa",
        " Sneha",
        "AMAN ",
        "priya",
        "VIKAS"
    ],
    "Department": [
        "AI",
        "HR",
        "AI",
        "Sales",
        "HR",
        "AI",
        "Sales",
        "AI"
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Nagpur",
        "Pune",
        "Delhi",
        "Mumbai",
        "Delhi",
        "Nagpur"
    ],
    "Salary": [
        65000,
        48000,
        np.nan,
        52000,
        50000,
        70000,
        56000,
        68000
    ],
    "Experience": [
        2,
        1,
        3,
        2,
        np.nan,
        4,
        2,
        5
    ],
    "Joining_Date": [
        "2023-01-15",
        "2022-06-10",
        "2024-03-20",
        "2021-11-05",
        "2022-09-18",
        "2020-08-12",
        "2023-05-09",
        "2019-02-25"
    ]
}

df = pd.DataFrame(employees)

print("=" * 50)
print("EMPLOYEE DATA ANALYTICS SYSTEM")
print("=" * 50)

# ========================================================================
# Original DataFrame
# ========================================================================

print("\nOriginal DataFrame: ")
print(df.to_string(index = False))

# ========================================================================
# Data Cleaning
# ========================================================================

df["Name"] = df["Name"].str.strip().str.title()
df["Department"] = df["Department"].str.upper()

print("\nData Information")
df.info()

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
print("\nData Types")
print(df.dtypes)

# ========================================================================
# Missing Values
# ========================================================================

print("\nMissing Values: ")
print(df.isnull().sum())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

print("\nFilled Missing Values Successfully!")

# ========================================================================
# Statistics Summary
# ========================================================================

print("\nStatistics Summary: ")

print(f"\nHighest Salary: {df['Salary'].max():,.2f}" )

print(f"\nLowest Salary: {df['Salary'].min():,.2f} ")

print(f"\nAverage Salary: {df['Salary'].mean():,.2f}")

print(f"\nTotal Salary: {df['Salary'].sum():,.2f}")

print(f"\nTotal Employees: {df['Name'].count()}")

# ========================================================================
# Filtering and Sorting
# ========================================================================

print("\nEmployees with Salary > 60000: ")
print(df[df["Salary"] > 60000])

print("\nEmployees in AI Department: ")
print(df[df["Department"] == "AI"])

print("\nEmployees with experience >= 3: ")
print(df[df["Experience"] >= 3])

print("\nSorted by salary (Descending): ")
print(df.sort_values(by = "Salary", ascending = False))

# ========================================================================
# Group by and Aggregation
# ========================================================================

print("\nDepartment-wise Salary Analysis: ")
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum", "count"]))

# ========================================================================
# Date and Time Operations
# ========================================================================

df["Year"] = df["Joining_Date"].dt.year
print("\nJoining Year: ")
print(df["Year"])

df["Month"] = df["Joining_Date"].dt.month
print("\nJoining Month: ")
print(df["Month"])

df["Day"] = df["Joining_Date"].dt.day
print("\nJoining Day: ")
print(df["Day"])

df["Day_Name"] = df["Joining_Date"].dt.day_name()
print("\nJoining Day Name: ")
print(df["Day_Name"])

today = pd.Timestamp.today()
df["Days_Worked"] = (today - df["Joining_Date"]).dt.days

print("\nDays Worked: ")
print(df["Days_Worked"])

# ========================================================================
# Merge DataFrames
# ========================================================================

manager = {
    "Department": ["AI","HR","SALES"],
    "Manager": [
        "Rahul",
        "Neha",
        "Arjun"
    ]
}

df2 = pd.DataFrame(manager)
print("\nDepartment Manager Mapping:")
print(df2)

df = pd.merge(df, df2, on = "Department", how = "inner")

print("\nFinal DataFrame: ")
print(df.to_string(index = False))

print("\n" + "=" * 50)
print("Analysis Completed Successfully!")
print("=" * 50)