import pandas as pd

df = pd.read_csv("supermarket_sales_150 - Sheet1.csv")

print(df.head())
print(df.columns)
print(df.info())
print(df.isnull().sum())
print("Duplicate records:", df.duplicated().sum())
df["Date"] = pd.to_datetime(df["Date"])

print(df["Date"].dtype)
df["Customer Type"] = df["Customer Type"].fillna("Unknown")
df["Gender"] = df["Gender"].fillna("Unknown")
df["Payment Method"] = df["Payment Method"].fillna("Unknown")

print(df.isnull().sum())
print("Invalid Unit Price:", (df["Unit Price"] <= 0).sum())
print("Invalid Quantity:", (df["Quantity"] <= 0).sum())
print("Invalid Total Sales:", (df["Total Sales"] <= 0).sum())
print("Duplicate records:", df.duplicated().sum())
print("Final Dataset Shape:", df.shape)
print("Total Missing Values:", df.isnull().sum().sum())
print("Total Duplicate Records:", df.duplicated().sum())
df.to_csv("cleaned_supermarket_sales.csv", index=False)
print("Cleaned dataset saved successfully.")
print("\nDescriptive Statistics:")
print(df.describe())
print("\nDataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)
print("\nDataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)
print("\nCorrelation Matrix:")
print(df[["Unit Price", "Quantity", "Total Sales"]].corr())
print("\nSales by Product Category:")
print(df.groupby("Product Category")["Total Sales"].sum().sort_values(ascending=False))

print("\nSales by Customer Type:")
print(df.groupby("Customer Type")["Total Sales"].sum().sort_values(ascending=False))

print("\nSales by Payment Method:")
print(df.groupby("Payment Method")["Total Sales"].sum().sort_values(ascending=False))
print("\nOutlier Analysis:")

for column in ["Unit Price", "Quantity", "Total Sales"]:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower_limit) | (df[column] > upper_limit)]

    print(f"{column} Outliers:", len(outliers))
    print("\nEDA Findings:")

print("Average Total Sales:", df["Total Sales"].mean())
print("Highest Total Sales:", df["Total Sales"].max())
print("Average Quantity:", df["Quantity"].mean())
print("Average Unit Price:", df["Unit Price"].mean())

print("\nHighest Selling Product Category:")
print(df.groupby("Product Category")["Total Sales"].sum().idxmax())

print("\nMost Used Payment Method:")
print(df["Payment Method"].value_counts().idxmax())

print("\nMost Common Customer Type:")
print(df["Customer Type"].value_counts().idxmax())
print("\nEDA Findings:")

print("Average Total Sales:", df["Total Sales"].mean())
print("Highest Total Sales:", df["Total Sales"].max())
print("Average Quantity:", df["Quantity"].mean())
print("Average Unit Price:", df["Unit Price"].mean())

print("\nHighest Selling Product Category:")
print(df.groupby("Product Category")["Total Sales"].sum().idxmax())

print("\nMost Used Payment Method:")
print(df["Payment Method"].value_counts().idxmax())

print("\nMost Common Customer Type:")
print(df["Customer Type"].value_counts().idxmax())
print("\nEDA Findings:")

print("Average Total Sales:", df["Total Sales"].mean())
print("Highest Total Sales:", df["Total Sales"].max())
print("Average Quantity:", df["Quantity"].mean())
print("Average Unit Price:", df["Unit Price"].mean())

print("\nHighest Selling Product Category:")
print(df.groupby("Product Category")["Total Sales"].sum().idxmax())

print("\nMost Used Payment Method:")
print(df["Payment Method"].value_counts().idxmax())

print("\nMost Common Customer Type:")
print(df["Customer Type"].value_counts().idxmax())