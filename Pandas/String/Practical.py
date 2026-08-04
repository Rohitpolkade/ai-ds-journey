import pandas as pd

employees = {
    "Name": [" rohit ", "KABIR", "dev", "RuDa","  Sneha","AMAN "],
    "Email": ["rohit@gmail.com", "kabir@Yahoo.com", "DEV@GMAIL.COM", "ruda@outlook.com","Sneha@gmail.com", "aman@Yahoo.com"],
    "Department": ["AI", "CSE", "ai", "HR", "CSE", "Ai"],
    "City": ["Pune", "Mumbai", "Nagpur", "Pune", "Delhi", "Mumbai"]
}

df = pd.DataFrame(employees)

print("=" * 50)
print("EMPLOYEE CONTACT CLEANER")
print("=" * 50)

print("Original DataFrame: ")
print(df)

df["Department"] = df["Department"].str.upper()
print("\nUppercase Department: ")
print(df)

df["Email"] = df["Email"].str.lower()
print("\nLowercase Email: ")
print(df)

df["Name"] = df["Name"].str.title()
print("\nTitlecase Names: ")
print(df)

df["Name"] = df["Name"].str.strip()
print("\nNames After Removing spaces: ")
print(df)

df["Email"] = df["Email"].str.replace("gmail", "company")
print("\nUpdated Emails: ")
print(df)

print("\nName Length: ")
print(df["Name"].str.len())

print("\nString contains 'gmail': ")
print(df["Email"].str.contains("gmail"))

print("\nSplit Email: ")
print(df["Email"].str.split("@"))