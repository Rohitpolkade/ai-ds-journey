import pandas as pd

df = pd.read_csv(r"C:\Users\rohit\GitHub\AI-Journey\Pandas\Reading&Writing\products.csv", encoding = "latin1")

print(df)
print("\nFirst 5 rows: \n", df.head())
print("\nLast 5 rows: \n", df.tail())

print("\nDimensions: \n", df.shape)
print("\nColumns: \n", df.columns)
print("\nDatatypes: \n", df.dtypes)

print("\nInformation related Dataframe: \n", df.info())
print("\nDescription related Dataframe: \n", df.describe())

df.to_csv("products_backup.csv", index = False)