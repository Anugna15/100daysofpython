import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('iris.csv')

# Initial Inspection
print("First 5 Rows:\n", df.head())
print("\n Missing Values per Column:\n", df.isnull().sum())
print("\n Dataset Info:")
df.info()

# Summary statistics
print(" Summary Statistics:\n", df.describe())

# Handling missing values
if df.isnull().values.any():
    print("\n🛠 Filling Missing Values with 0...")
    df.fillna(0, inplace=True)
    print(df.isnull().sum())
else:
    print("\n No missing values found!")

# Final data preview
print("\n Final Data Preview:\n", df.head())

print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Mode:\n", df.mode(numeric_only=True).iloc[0])

print("Variance:\n", df.var(numeric_only=True))
print("Standard Deviation:\n", df.std(numeric_only=True))

print("Minimum:\n", df.min(numeric_only=True))
print("Maximum:\n", df.max(numeric_only=True))
print("Range:\n", df.max(numeric_only=True) - df.min(numeric_only=True))

print("Skewness:\n", df.skew(numeric_only=True))
print("Kurtosis:\n", df.kurt(numeric_only=True))

print("Correlation Matrix:\n", df.corr(numeric_only=True))
