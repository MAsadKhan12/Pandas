#Lets work on csv files
import pandas as pd
csv_path='check.csv'
df=pd.read_csv(csv_path)
df.head()
x=df.head() #Load first five rows of data frames
print(x)


