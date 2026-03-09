import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("C:/Users/asmit/OneDrive/Desktop/ola-ride-insights/dataset/ola_cleaned.csv")

print(df.head())

plt.figure(figsize=(8,5))
sns.histplot(df["Customer_Rating"], bins=20)
plt.title("Customer Ratings Distribution")
plt.show()
