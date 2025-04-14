# Day 8: Feature Engineering - In-Depth Notes

## 1. What is Feature Engineering?
Feature Engineering is the process of using domain knowledge to extract features (input variables) from raw data to improve model performance. It includes:
- Feature Selection
- Feature Extraction
- Feature Scaling

---

## 2. Feature Selection
Feature Selection helps in identifying the most significant features that contribute to predicting the target variable.

### Techniques:
- **Univariate Selection (SelectKBest)**
  - It selects the top k features that have the strongest relationship with the target variable.

### Code Example:
```python
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k=2)
X_new = selector.fit_transform(X, y)
print("Selected features shape:", X_new.shape)
```

---

## 3. Feature Scaling
Feature Scaling standardizes the range of features, especially when features have different units.

### Why it's important:
- Many ML algorithms (e.g., k-NN, SVM, gradient descent-based models) are sensitive to feature scales.

### Types:
- **Standardization (Z-score scaling)**
  - Mean = 0, Std Dev = 1
- **Normalization (Min-Max scaling)**
  - Range = [0, 1]

### Code Example:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 4. End-to-End Practical Example
Using the Wine dataset:

```python
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load Data
data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Feature Selection
X = df.drop('target', axis=1)
y = df['target']
selector = SelectKBest(score_func=f_regression, k=5)
X_selected = selector.fit_transform(X, y)

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_selected)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))
```

