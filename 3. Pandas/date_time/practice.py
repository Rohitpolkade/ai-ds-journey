import pandas as pd

employees = {
    "Name": ["Rohit", "Kabir", "Dev", "Sneha", "Aman"],
    "Joining_Date": [
        "2023-01-15",
        "2022-08-20",
        "2024-03-12",
        "2021-10-05",
        "2020-07-18"
    ]
}

df = pd.DataFrame(employees)

print("=" * 50)
print("EMPLOYEE JOINING DATE ANALYZER")
print("=" * 50)

print("\nOriginal DataFrame: ")
print(df)

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
print("\nConverted DataFrame: ")
print(df)

df["Year"] = df["Joining_Date"].dt.year
print("\nJoining Years: ")
print(df["Year"])

df["Month"] = df["Joining_Date"].dt.month
print("\nJoining Months: ")
print(df["Month"])

df["Day"] = df["Joining_Date"].dt.day
print("\nJoining Days: ")
print(df["Day"])


df["Day_Name"] = df["Joining_Date"].dt.day_name()
print("\nDay Names: ")
print(df["Day_Name"])

today = pd.Timestamp.today()
df["Days_Worked"] = (today - df["Joining_Date"]).dt.days

print("\nDays Worked: ")
print(df["Days_Worked"])

print("\nFinal DataFrame: ")
print(df)