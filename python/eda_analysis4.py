import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("C:/Users/asmit/OneDrive/Desktop/ola-ride-insights/dataset/ola_cleaned.csv")

print(df.head())

plt.figure(figsize=(6,6))
df["Payment_Method"].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Payment Method Distribution")
plt.show()