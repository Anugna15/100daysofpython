import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('iris.csv')
print(df['species'].value_counts())
print(df.head())
df['species'].value_counts().plot(kind='bar', color='skyblue', figsize=(8, 4))
plt.title('Species Count')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

sns.boxplot(data=df.select_dtypes(include='number'))
plt.title("Boxplot of Numerical Features")
plt.show()

sns.pairplot(df, hue='species', palette='Set2')
plt.title("Pairplot of Features")
plt.show()

corr = df.corr(numeric_only=True)

# Plot the heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

plt.plot(df['sepal_length'], label='Sepal Length')
plt.plot(df['petal_length'], label='Petal Length')
plt.legend()
plt.title('Line Plot of Sepal & Petal Length')
plt.show()

df.to_csv("iris_cleaned.csv", index=False)

