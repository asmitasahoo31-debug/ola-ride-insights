import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("C:/Users/asmit/OneDrive/Desktop/ola-ride-insights/dataset/ola_cleaned.csv")
print(df.head())

plt.figure(figsize=(8,5))
sns.countplot(x="Vehicle_Type", data=df)
plt.title("Vehicle Type Demand")
plt.xticks(rotation=45)
plt.show()