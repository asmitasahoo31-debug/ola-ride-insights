import pandas as pd

# Load dataset
df = pd.read_excel("C:/Users/asmit/OneDrive/Desktop/ola-ride-insights/dataset/OLA_DataSet .xlsx")

print("Dataset Loaded Successfully")

# Show first rows
print(df.head())

# Dataset info
print("\nDataset Info")
print(df.info())

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create new columns
df["Day"] = df["Date"].dt.day_name()
df["Month"] = df["Date"].dt.month_name()

# Convert rating columns to numeric
df["Driver_Ratings"] = pd.to_numeric(df["Driver_Ratings"], errors="coerce")
df["Customer_Rating"] = pd.to_numeric(df["Customer_Rating"], errors="coerce")

# Fill missing ratings
df["Driver_Ratings"] = df["Driver_Ratings"].fillna(df["Driver_Ratings"].mean())
df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].mean())

# Remove unnecessary column
if "Vehicle Images" in df.columns:
    df = df.drop(columns=["Vehicle Images"])

# Fix V_TAT and C_TAT columns
df["V_TAT"] = pd.to_numeric(df["V_TAT"], errors="coerce")
df["C_TAT"] = pd.to_numeric(df["C_TAT"], errors="coerce")

# Replace NaN with 0 (or you can keep NULL)
df["V_TAT"] = df["V_TAT"].fillna(0)
df["C_TAT"] = df["C_TAT"].fillna(0)

# Save cleaned dataset
df.to_csv("C:/Users/asmit/OneDrive/Desktop/ola-ride-insights/dataset/ola_cleaned.csv", index=False)

print("\nClean dataset saved successfully")