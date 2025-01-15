import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/DISHA WAGHMARE/OneDrive/Documents/heart_attack_dataset.csv')

# Set the style for better visuals
sns.set(style="whitegrid")

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart for Gender distribution
gender_counts = df['Gender'].value_counts()
sns.barplot(x=gender_counts.index, y=gender_counts.values, ax=axes[0], palette="pastel")
axes[0].set_title("Distribution of Gender", fontsize=14)
axes[0].set_xlabel("Gender", fontsize=12)
axes[0].set_ylabel("Count", fontsize=12)

# Histogram for Age distribution
sns.histplot(df['Age'], bins=10, kde=True, color="skyblue", ax=axes[1])
axes[1].set_title("Distribution of Age", fontsize=14)
axes[1].set_xlabel("Age", fontsize=12)
axes[1].set_ylabel("Frequency", fontsize=12)

# Adjust layout for better visualization
plt.tight_layout()
plt.show()
