import pandas as pd
import numpy as np
data=pd.series([1,2,4,np.nan,8,9])
print(data)
print(data.isnull()) # check for null values
print(data.notnull()) # check for non-null values
print(data.dropna()) # drop null values
print(data.fillna(0)) # fill null values with 0
print(data.fillna(method='ffill')) # fill null values with forward fill
print(data.shape) # check the shape of the data
print(data.size) # check the size of the data
print(data.index) # check the index of the data
print(data.values) # check the values of the data
print(data.dtype) # check the data type of the data
print(data.head()) # check the first 5 rows of the data
print(data.tail()) # check the last 5 rows of the data
print(data.sample(3)) # check 3 random rows of the data
print(data.describe()) # check the summary of the data
print(data.info()) # check the info of the data
print(data.memory_usage()) # check the memory usage of the data
print(data.nunique()) # check the number of unique values in the data
print(data.value_counts()) # check the value counts of the data

