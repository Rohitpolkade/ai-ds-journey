import pandas as pd

# read data from CSV, Excel, Json file into a Dataframe

df = pd.read_csv(r"Pandas\Reading&Writing\sales_data_sample.csv", encoding = "latin1")
df = pd.read_excel(r"Pandas\Reading&Writing\SampleSuperstore.xlsx")
df = pd.read_json(r"Pandas\Reading&Writing\sample_Data.json")

print(df)

print("Display 10 rows of first:")
print(df.head(10))

print("Display 10 rows of last:")
print(df.tail(10))

print(df.info())
print(df.describe())


data = {
    "Name" : ["Rohit", "Ram", "Mrunal"],
    "Age" : [20, 21, 20],
    "Marks" : [90, 95, 85]
}

dataframe = pd.DataFrame(data)

print(dataframe)

# save data
dataframe.to_csv("Pandas\Reading&Writing\Output.csv", index = False)
dataframe.to_excel("Pandas\Reading&Writing\Output.xlsx", index = False)
dataframe.to_json("Pandas\Reading&Writing\Output.json", index = False)