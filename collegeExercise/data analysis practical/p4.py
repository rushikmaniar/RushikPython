import pandas as pd 

# assigning three series to s1, s2, s3 
s1 = pd.Series([0, 4, 8]) 
s2 = pd.Series([1, 5, 9]) 
s3 = pd.Series([2, 6, 10]) 

# taking index and column values 
dframe = pd.DataFrame([s1, s2, s3]) 

# assign column name 
dframe.columns =['col1', 'col2', 'col3'] 

# write data to csv file 
dframe.to_csv('testing1.csv', index = False) 
dframe.to_csv('testing2.csv', index = True) 
