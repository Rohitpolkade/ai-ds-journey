import pandas as pd

employees = {
      "Name": ["Rohit", "Kabir", "Dev", "Sneha"],
    "Joining_Date": [
        "2023-01-15",
        "2022-06-10",
        "2024-02-20",
        "2021-11-05"
    ]
}

df = pd.DataFrame(employees)

print(df)

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print()
print(df["Joining_Date"].dt.year)

print()
print(df["Joining_Date"].dt.month)

print()
print(df["Joining_Date"].dt.day)

print()
print(df["Joining_Date"].dt.day_name())

today = pd.Timestamp.today()

df["Days_Worked"] = (today - df["Joining_Date"]).dt.days

print()
print(df)