import pandas as pd

# Load the dataset
df = pd.read_csv("AI_Skin_Product..csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Display total number of products
print("Total Products:", len(df))

# Count products by skin type
print(df["Skin_Type"].value_counts())

# Count products by concern
print(df["Concern"].value_counts())

import matplotlib.pyplot as plt

# Products by skin type
df["Skin_Type"].value_counts().plot(kind="bar")

plt.title("Products by Skin Type")
plt.xlabel("Skin Type")
plt.ylabel("Number of Products")

plt.show()

# AI Skin Product Recommendation

skin_type = input("Enter your skin type: ")
concern = input("Enter your skin concern: ")

result = df[
    (df["Skin_Type"].str.lower() == skin_type.lower()) &
    (df["Concern"].str.lower() == concern.lower())
]

print("\nRecommended Products:")
print(result[["Product", "Price", "Features"]])

print(df.groupby(["Skin_Type","Concern"].size()))