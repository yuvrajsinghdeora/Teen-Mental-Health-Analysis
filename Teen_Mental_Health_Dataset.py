import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(r"C:\Users\deora\OneDrive\Desktop\Python Project\Teen_Mental_Health_Dataset.csv")

# Style
sns.set_style("whitegrid")

print("Dataset Shape:", df.shape)
print(df.head())

# 1. Gender Distribution
plt.figure(figsize=(6,6))
df['gender'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# 2. Platform Usage
plt.figure(figsize=(8,5))
sns.countplot(
    x='platform_usage',
    data=df,
    order=df['platform_usage'].value_counts().index
)
plt.title("Platform Usage Distribution")
plt.xticks(rotation=45)
plt.show()

# 3. Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['age'], bins=10, kde=True)
plt.title("Age Distribution")
plt.show()

# 4. Daily Social Media Hours
plt.figure(figsize=(8,5))
sns.histplot(df['daily_social_media_hours'], bins=20, kde=True)
plt.title("Daily Social Media Usage")
plt.show()

# 5. Sleep Hours
plt.figure(figsize=(8,5))
sns.histplot(df['sleep_hours'], bins=15, kde=True)
plt.title("Sleep Hours Distribution")
plt.show()

# 6. Stress Level
plt.figure(figsize=(8,5))
sns.histplot(df['stress_level'], bins=10, kde=True)
plt.title("Stress Level Distribution")
plt.show()

# 7. Anxiety Level
plt.figure(figsize=(8,5))
sns.histplot(df['anxiety_level'], bins=10, kde=True)
plt.title("Anxiety Level Distribution")
plt.show()

# 8. Addiction Level
plt.figure(figsize=(8,5))
sns.histplot(df['addiction_level'], bins=10, kde=True)
plt.title("Addiction Level Distribution")
plt.show()

# 9. Correlation Heatmap
plt.figure(figsize=(10,8))
numeric_df = df.select_dtypes(include='number')

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap")
plt.show()

# 10. Social Media Hours vs Stress
plt.figure(figsize=(8,5))

sns.regplot(
    x='daily_social_media_hours',
    y='stress_level',
    data=df,
    scatter_kws={'alpha':0.4}
)

plt.title("Social Media Hours vs Stress Level")
plt.show()

# 11. Sleep Hours vs Anxiety
plt.figure(figsize=(8,5))
sns.scatterplot(
    x='sleep_hours',
    y='anxiety_level',
    data=df
)
plt.title("Sleep Hours vs Anxiety Level")
plt.show()

# 12. Stress Level by Gender
plt.figure(figsize=(8,5))
sns.boxplot(
    x='gender',
    y='stress_level',
    data=df
)
plt.title("Stress Level by Gender")
plt.show()

# 13. Academic Performance vs Addiction
plt.figure(figsize=(8,5))
sns.scatterplot(
    x='academic_performance',
    y='addiction_level',
    data=df
)
plt.title("Academic Performance vs Addiction Level")
plt.show()

# 14. Physical Activity vs Stress
sns.regplot(
    x='physical_activity',
    y='stress_level',
    data=df,
    scatter_kws={'alpha':0.4}
)
plt.title("Physical Activity vs Stress")
plt.show()

print("Project Completed Successfully!")