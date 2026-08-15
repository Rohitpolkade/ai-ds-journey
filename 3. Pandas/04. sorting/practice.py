import pandas as pd

students = {
    "Name": ["Rohit", "Kabir", "Dev", "Ruda", "Sneha", "Aman"],
    "Age": [20, 20, 21, 22, 19, 21],
    "Marks": [90, 82, 95, 88, 76, 91]
}

df = pd.DataFrame(students)
print("=" * 50)
print("STUDENT MARKS ANALYZER")
print("=" * 50)

print("\nOriginal Dataframe:")
print(df)

print("\nSorted by Marks (Ascending):")
print(df.sort_values(by = "Marks"))

print("\nSorted by Marks (Descending):")
print(df.sort_values(by = "Marks", ascending = False))

print("\nSorted by Age & Marks:")
print(df.sort_values(by = ["Age", "Marks"]))

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

print("\nAverage Marks:")
print(f"{df["Marks"].mean():.2f}")

print("\nTotal Marks:")
print(df["Marks"].sum())

print("\nTotal Students:")
print(df["Name"].count())

print("\nUnique Ages:")
print(df["Age"].unique())

print("\nNumber of Unique Ages:")
print(df["Age"].nunique())


