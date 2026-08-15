import pandas as pd

'''Filtering'''

students = {
    "Name" : ["Rohit", "Kabir", "Dev"],
    "Marks" : [90, 85, 80],
    "Age" : [20, 19, 18]
}

df  = pd.DataFrame(students)

print("DataFrame: \n",df)

# selecting multiple columns
print("\nName &  Marks Column: \n", df[["Name", "Marks"]])

# Boolean Filtering
print("\nStudent above 85: \n", df[df["Marks"] >= 85])
print("\nAbove 85 and Age geater than 21: \n",df[(df["Marks"] > 85) & (df["Age"] >= 20)])

# usage of loc
print("\nAll Rows and Two column: \n", df.loc[:, ["Name", "Marks"]])
print("\nOnly Rows: \n", df.loc[[0, 2]])
