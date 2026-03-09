import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("C:/Users/asmit/OneDrive/Desktop/ola-ride-insights/dataset/ola_cleaned.csv")

print(df.head())


plt.figure(figsize=(8,6))
sns.scatterplot(x="Driver_Ratings", y="Customer_Rating", data=df)
plt.title("Customer vs Driver Ratings")
plt.show()