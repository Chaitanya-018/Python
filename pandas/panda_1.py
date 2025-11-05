"""
PANDAS COMPLETE NOTES (With Sample Output)
------------------------------------------
Datasets used:
1. orders.csv   - Sales dataset
2. netflix.csv  - Netflix movies dataset

This script demonstrates essential pandas operations grouped by category.
"""

import pandas as pd

# ------------------------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------------------------
orders_df = pd.read_csv("orders.csv")
netflix_df = pd.read_csv("netflix.csv")

print("✅ Data Loaded Successfully")

# ------------------------------------------------------------------------------
# BASIC DATAFRAME INSPECTION
# ------------------------------------------------------------------------------
print("\n🔹 HEAD (Top 5 rows)")
print(orders_df.head())          # Sample Output:
#    order_id    sales    region
# 0  CA-201      200.5     South
# 1  US-120      150.0     West
# ...

print("\n🔹 TAIL (Last 5 rows)")
print(orders_df.tail())          # Shows bottom rows

print("\n🔹 SHAPE (rows, columns)")
print(orders_df.shape)           # Output: (999, 8)

print("\n🔹 COLUMNS")
print(orders_df.columns)
# Output: Index(['order_id', 'sales', 'region', ...])

print("\n🔹 DATA TYPES")
print(orders_df.dtypes)
# Output:
# order_id     object
# sales        float64
# region       object

print("\n🔹 INFO")
orders_df.info()
# Shows column datatype, non-null count

print("\n🔹 DESCRIBE (Summary of numerical columns)")
print(orders_df.describe())
# Output includes: count, mean, std, min, max

# ------------------------------------------------------------------------------
# COLUMN SELECTION
# ------------------------------------------------------------------------------

print("\n🔹 Selecting a single column:")
print(orders_df["region"].head())
# Output: first 5 values of region column

print("\n🔹 Selecting multiple columns:")
print(orders_df[["order_id", "sales"]].head())
# Output: order_id and sales columns

# ------------------------------------------------------------------------------
# SLICING AND INDEXING
# ------------------------------------------------------------------------------

print("\n🔹 loc (label based indexing)")
print(orders_df.loc[0, "sales"])
# Output: 200.5

print("\n🔹 iloc (index based indexing)")
print(orders_df.iloc[2, 3])
# Output: value from row index 2, col index 3

print("\n🔹 at / iat (Faster for single cell access)")
print(orders_df.iat[4, 2])       # value in row 4 col 2

# ------------------------------------------------------------------------------
# FILTERING / BOOLEANS / QUERY
# ------------------------------------------------------------------------------

print("\n🔹 Boolean Filtering (AND condition)")
print(orders_df[(orders_df["region"] == "West") & (orders_df["sales"] > 300)].head())
# Output sample rows: only where region is West AND sales > 300

print("\n🔹 OR condition")
print(orders_df[(orders_df["region"] == "South") | (orders_df["sales"] > 500)].head())

print("\n🔹 Using query()")
print(orders_df.query("region == 'South'").head())

print("\n🔹 between()")
print(orders_df[orders_df["sales"].between(100, 200)].head())

# ------------------------------------------------------------------------------
# NULL / DUPLICATES / CLEANING
# ------------------------------------------------------------------------------

print("\n🔹 Check null values (True/False mask)")
print(orders_df.isnull().head())

print("\n🔹 Drop rows with null values")
print(orders_df.dropna().head())

print("\n🔹 Fill empty values")
print(orders_df.fillna("Unknown").head())

print("\n🔹 Remove duplicate rows")
print(orders_df.drop_duplicates().head())

# ------------------------------------------------------------------------------
# SORTING
# ------------------------------------------------------------------------------

print("\n🔹 Sort values (highest sales first)")
print(orders_df.sort_values("sales", ascending=False).head())

# ------------------------------------------------------------------------------
# GROUPBY (Aggregation)
# ------------------------------------------------------------------------------

print("\n🔹 Group by region and calculate avg sales")
print(orders_df.groupby("region")["sales"].mean())
# Output:
# region
# South     210.5
# West      190.2
# ...

# ------------------------------------------------------------------------------
# MERGING / CONCAT
# ------------------------------------------------------------------------------

# Example simple merge (dummy, if merging with netflix_df)
# merged_df = pd.merge(orders_df, netflix_df, how="inner", on="Votes")

# ------------------------------------------------------------------------------
# NETFLIX DATA CLEANING (RENAMING + TYPE CONVERSION)
# ------------------------------------------------------------------------------

print("\n🔹 Original datatypes of Netflix CSV:")
print(netflix_df.dtypes)

# Change datatypes
netflix_df["Duration"] = netflix_df["Duration"].astype(float)
netflix_df["Votes"] = netflix_df["Votes"].astype(str)

print("\n🔹 Rename columns")
netflix_df.rename(columns={"Duration": "Dur"}, inplace=True)

print("\n🔹 Cleaned Netflix DataFrame Sample:")
print(netflix_df.head())
# Output:
#        Title          Dur  Votes
# 0     Movie A         120  3000
# 1     Movie B          90  5000

print("\n✅ All operations completed successfully")
