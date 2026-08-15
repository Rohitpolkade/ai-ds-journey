import pandas as pd

marks = pd.Series([75, 82, 91, 68, 95])


print("---Series---\n")
print(marks)

print(f"\nMaximum:", marks.max())
print("Minimum:", marks.min())
print("Average:", marks.mean())

students = {
    "Name" : ["Rohit", "Kabir", "Dev", "Ruda"],
    "Age" : [20, 20, 21, 22],
    "Marks" : [90, 82, 95, 88]
}

print("\n---DataFrame---")
df = pd.DataFrame(student)

print(f"\n{df}\n")
print("shape: \n", df.shape)
print("\nColumn: \n", df.columns)
print("\nData Types: \n", df.dtypes)

# Access columns
print("\nName Column: \n", df["Name"])
print("\nMarks Column: \n", df["Marks"])
print("\nName & Marks Column: \n", df[["Name","Marks"]])

print("\nFirst Student: \n", df.iloc[0])
print("\nThird Rows: \n", df.iloc[2])


