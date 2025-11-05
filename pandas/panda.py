import pandas as pd

"""
Pandas Basics
-------------
1. Series  → 1-D data
2. DataFrame → 2-D data (rows + columns)
"""

# -----------------------------------------
# Creating DataFrame and Series (Examples)
# -----------------------------------------

details = {
    "names": ["chaitu", "ganesh", "rohith", "bhargav"],
    "marks": [0, 35, 90, 36]
}

df = pd.DataFrame(details)
print("\n✅ DataFrame Example:")
print(df)

series_example = pd.Series([1, 2, 3, 4])
print("\n✅ Series Example:")
print(series_example)

# ------------------------------------------------
# DataFrame Methods (Reading CSV and basic methods)
# ------------------------------------------------

df = pd.read_csv("orders.csv")

print("\n🔹 Top Rows (df.head()):")
print(df.head())

print("\n🔹 Bottom Rows (df.tail()):")
print(df.tail())

print("\n🔹 DataFrame Info (df.info()):")
print(df.info())

print("\n🔹 Numerical Summary (df.describe()):")
print(df.describe())

print("\n🔹 Shape (rows, columns):")
print(df.shape)

print("\n🔹 Column names:")
print(df.columns)

print("\n🔹 Data Types of columns:")
print(df.dtypes)

# ------------------------------------------------
# Indexing and Selection (loc, iloc, at, iat)
# ------------------------------------------------

print("\n🔹 Using loc (label-based indexing):")
print(df.loc[0, "region"])    # Value at row 0, column 'region'

print("\n🔹 Using iloc (integer index):")
print(df.iloc[1, 1])          # Value at row 1, column index 1

print("\n🔹 Fast access using iat:")
print(df.iat[2, 3])           # Faster for a single value

# ------------------------------------------------
# Filtering / Query / Boolean Masking
# ------------------------------------------------

print("\n🔹 Using query():")
print(df.query('ship_mode == "Second Class" and region == "South"'))

print("\n🔹 Boolean Indexing:")
print(df[(df['ship_mode'] == "Second Class") | (df['region'] == "South")])

print("\n🔹 Using between(): Profit between 5 and 10")
print(df[df["profit"].between(5, 10)])

# ------------------------------------------------
# Handling Missing & Duplicate Data
# ------------------------------------------------

print("\n🔹 Checking null values (df.isnull()):")
print(df.isnull())

print("\n🔹 Dropping null values (dropna):")
print(df.dropna())

print("\n🔹 Filling null values (fillna):")
print(df.fillna("NA"))

print("\n🔹 Removing duplicate rows:")
print(df.drop_duplicates())

# ------------------------------------------------
# Data Cleaning: astype() and rename()
# ------------------------------------------------

netflix = pd.read_csv("netflix.csv")

# Change data types
netflix["Duration"] = netflix["Duration"].astype(float)
netflix["Votes"] = netflix["Votes"].astype(str)

# Rename column
netflix.rename(columns={"Duration": "Dur"}, inplace=True)

print("\n✅ Final Cleaned Netflix DataFrame:")
print(netflix)
