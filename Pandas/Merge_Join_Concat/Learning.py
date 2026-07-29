import pandas as pd

# merge()
students = pd.DataFrame({
    "ID" : [1, 2, 3],
    "Name" : ["Rohit", "Aman", "Priya"]
})

marks = pd.DataFrame({
    "ID" : [1, 2, 3],
    "Marks" : [90, 91, 92]
})

df = pd.merge(students, marks, on = "ID")
print(df)

print()
print(df["Name"])

# join()
dept = pd.DataFrame({
    "Department": ["AI", "CSE", "HR"]
}, index=[1, 2, 3])

salary = pd.DataFrame({
    "Salary": [60000, 70000, 50000]
}, index=[1, 2, 3])

joined = dept.join(salary)
print(joined)

# concat()

import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Rohit", "Aman"]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Sneha"]
})

concat_vertically = pd.concat([df1, df2], axis = 0, ignore_index = True)
print(concat_vertically)

concat_horizantally = pd.concat([students, marks], axis = 1)
print()
print(concat_horizantally)