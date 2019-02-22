# import the required module 
import matplotlib.pyplot as plt
# Import the pandas library, renamed as pd 
import pandas as pd 

# Read IND_data.csv into a DataFrame, assigned to df 
df = pd.read_csv("IND_data.csv") 

# Prints the first 5 rows of a DataFrame as default 
print(df.head())

# Prints no. of rows and columns of a DataFrame
print(df.shape)

# plot a histogram

df['Observation Value'].hist(bins=10) 
plt.show()

# shows presence of a lot of outliers/extreme values 
df.boxplot(column='Observation Value', by = 'Time period') 
plt.show()

# plotting points as a scatter plot 
x = df["Observation Value"]
y = df["Time period"] 
plt.scatter(x, y, label= "stars", color= "m", 
			marker= "*", s=30) 
# x-axis label 
plt.xlabel('Observation Value') 
# frequency label 
plt.ylabel('Time period') 
# function to show the plot 
plt.show() 
