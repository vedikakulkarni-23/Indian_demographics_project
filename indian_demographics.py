# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (replace 'your_dataset.csv' with your actual dataset path)
data = pd.read_csv('dataset.csv')

# Basic data overview
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset summary:")
print(data.info())

print("\nStatistical summary of numerical columns:")
print(data.describe())

# Checking for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Visualizing demographic trends (adjust columns to your dataset)
# Example 1: Age distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
# Example: Save the age distribution graph as an image
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('age_distribution.png')  # Save the graph as an image
plt.show()


# Example 2: Gender distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=data)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
# Example: Save the age distribution graph as an image
plt.figure(figsize=(8, 6))
sns.histplot(data['Gender'], bins=30, kde=True)
plt.title('Gender distribution')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.savefig('gender_distribution.png')  # Save the graph as an image
plt.show()


# Example 3: Region-wise population distribution (replace 'Region' with actual column name)
plt.figure(figsize=(12, 8))
data['Region'].value_counts().plot(kind='bar')
plt.title('Region-wise Population Distribution')
plt.xlabel('Region')
plt.ylabel('Count')
plt.show()
# Example: Save the age distribution graph as an image
plt.figure(figsize=(8, 6))
sns.histplot(data['Population'], bins=30, kde=True)
plt.title('Population Distribution')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.savefig('population_distribution.png')  # Save the graph as an image
plt.show()


# Example 4: Correlation heatmap (for numerical columns)
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
# Example: Save the age distribution graph as an image
plt.figure(figsize=(8, 6))
sns.histplot(data['Correlation Heatmap'], bins=30, kde=True)
plt.title('Correlation Heatmap')
plt.xlabel('Correlation Heatmap')
plt.ylabel('Frequency')
plt.savefig('correlation_Heatmap.png')  # Save the graph as an image
plt.show()

