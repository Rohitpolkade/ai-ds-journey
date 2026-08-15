import pandas as pd

marks = pd.Series([90, 85, 87, 92])
print(marks)

students = {
    "Name" : [ "Rohit", "Ram", "Mrunal"],
    "Marks" : [95, 90, 91],
    "Age" : [20, 21, 20]
}


df = pd.DataFrame(students)
# df = pd.Series(students)
print(df)

df_shape = df.shape
print(df_shape)

df_columns = df.columns
print(df_columns)

df_datatype = df.dtypes
print(df_datatype)

# selecting column
print(df["Name"])
df[["Name", "age"]]

# selecting rows
print(df.iloc[0])
print(df.iloc[1]) 