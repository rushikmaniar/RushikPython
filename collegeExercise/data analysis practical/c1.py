import pandas as pd
# Program to Create series with scalar values 
Data =[1, 3, 4, 5, 6, 2, 9] # Numeric data 

# Creating series with default index values 
s = pd.Series(Data)	 
print(s)

# predefined index values 
Index =['a', 'b', 'c', 'd', 'e', 'f', 'g'] 

# Creating series with predefined index values 
si = pd.Series(Data, Index)
print(si)
