import pandas as pd

employees = {
    "Name": [" rohit ", "KABIR", "dev", "RuDa","  Sneha","AMAN "],
    "Email": ["rohit@gmail.com", "kabir@Yahoo.com", "DEV@GMAIL.COM", "ruda@outlook.com","Sneha@gmail.com", "aman@Yahoo.com"],
    "Department": ["AI", "CSE", "ai", "HR", "CSE", "Ai"],
    "City": ["Pune", "Mumbai", "Nagpur", "Pune", "Delhi", "Mumbai"]
}

df = pd.DataFrame(employees)
print("Before Cleaning:")
print(df)

# Convert to Uppercase
df["Department"] = df["Department"].str.upper()
print()
print(df)

# Convert to Lowercase
df["Email"] = df["Email"].str.lower()
print()
print(df)

# capitalize the first letter of each word
df["Name"] = df["Name"].str.title()
print()
print(df)

# Remove Extra Spaces
df["Name"] = df["Name"].str.strip()
print()
print(df)

# Replace Text
df["Email"] = df["Email"].str.replace("gmail", "outlook")
print()  
print(df)

# Checking string if it contains any specific word
print()
print(df["Email"].str.contains("gmail"))

# String Lenght
print()
print(df["Name"].str.len())

# Split String
print()
print(df["Email"].str.split("@"))

df["Email"] = df["Email"].str.split("@")
print(df)