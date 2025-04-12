import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load the Wine dataset
wine = load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df['target'] = wine.target

# 1. Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# 2. Fill or drop missing values if any (for demonstration)
# (Here there are no missing values, but you can do this generally)
df.fillna(df.mean(numeric_only=True), inplace=True)

# 3. Check for duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")
df.drop_duplicates(inplace=True)

# 4. Optional: Check basic statistics for outliers
print("\nSummary statistics:\n", df.describe())

# 5. Feature Scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop('target', axis=1))
X = pd.DataFrame(scaled_features, columns=wine.feature_names)
y = df['target']

# Split the cleaned dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Visualization: Scatter plot
plt.scatter(y_test, y_pred, color='teal')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Wine Categories')
plt.grid(True)
plt.show()

# Pairplot
df_scaled = pd.DataFrame(X, columns=wine.feature_names)
df_scaled['target'] = y
sns.pairplot(df_scaled, hue='target')
plt.savefig('wine_pairplot.png')
plt.show()
