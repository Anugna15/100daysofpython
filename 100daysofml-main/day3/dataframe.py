import numpy as np
import pandas as pd
data = {
    'id': [1, 2, 3, 4],
    'name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
    'age': [20, 22, 25, 30],
    'score': [90, 0 , 88, 92]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull()) # check for null values
print(df.notnull()) # check for non-null values
print(df.dropna()) # drop null values
print(df.fillna(0)) # fill null values with 0

print(data['name']) # check the name column of the data
print(data['name'].unique()) # check the unique values of the name column
print(data['name'].value_counts()) # check the value counts of the name column
print(data['name'].nunique()) # check the number of unique values in the name column
print(data['name'].isnull()) # check the null values of the name column
print(data['name'].notnull()) # check the non-null values of the name column
print(data['name'].dropna()) # drop null values of the name column
print(data['name'].fillna(0)) # fill null values of the name column with 0
print(data['age'].sum()) # check the sum of the age column
print(data['age'].mean()) # check the mean of the age column
print(data['age'].median()) # check the median of the age column
print(data['age'].mode()) # check the mode of the age column
print(data['age'].min()) # check the min of the age column
print(data['age'].max()) # check the max of the age column
print(data['age'].std()) # check the std of the age column
print(data['age'].var()) # check the var of the age column
print(data['age'].quantile(0.25)) # check the 25th percentile of the age column