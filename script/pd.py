import pandas as pd 


data = pd.read_excel('test.xlsx')

for index,row in data.iterrows():
    print(row['file'])