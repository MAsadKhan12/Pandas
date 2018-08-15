import pandas as bbb

df=bbb.read_csv('check.csv')
print(df['Zip Code'].unique())
print(df['Zip Code']>93432)
