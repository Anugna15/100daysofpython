import pandas as pd
data={
    'id':[1,2,3,4],
    'name':['Tom','Jerry','Mickey','Donald'],
    'age':[20,22,25,30],
    'score':[90,0 , 88, 92]
}
df=pd.DataFrame(data)
print(df[['name','age']]) # check the name and age columns of the data

print(df[df['age']>22]) # check the name column of the data where age is greater than 22
print(df[df['name'].isin(['Tom','Jerry'])]) # check the name column of the data where name is Tom or Jerry
print(df[df['name'].str.contains('T')]) # check the name column of the data where name contains T
print(df[df['name'].str.startswith('T')]) # check the name column of the data where name starts with T
print(df[df['name'].str.endswith('y')]) # check the name column of the data where name ends with y
print(df[df['name'].str.len()>3]) # check the name column of the data where name length is greater than 3
print(df[df['name'].str.len()<3]) # check the name column of the data where name length is less than 3
print(df[df['name'].str.len()==3]) # check the name column of the data where name length is equal to 3
df['percentage']=df['score']*0.1 # check the percentage of the score column
print(df) # check the data

df.to_csv('day3.csv', index=False)
