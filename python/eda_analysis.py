import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("C:/Users/asmit/OneDrive/Desktop/ola-ride-insights/dataset/ola_cleaned.csv")

print(df.head())
plt.figure(figsize=(8,5))
sns.countplot(x="Day", data=df)
plt.title("Ride Volume by Day")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x="Vehicle_Type", data=df)
plt.title("Vehicle Type Demand")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(6,6))
df["Booking_Status"].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Booking Status Distribution")
plt.show()

plt.figure(figsize=(6,6))
df["Payment_Method"].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Payment Method Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["Ride_Distance"], bins=30)
plt.title("Ride Distance Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["Driver_Ratings"], bins=20)
plt.title("Driver Ratings Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df["Customer_Rating"], bins=20)
plt.title("Customer Ratings Distribution")
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x="Driver_Ratings", y="Customer_Rating", data=df)
plt.title("Customer vs Driver Ratings")
plt.show()