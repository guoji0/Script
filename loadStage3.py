# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 18:22:54 2022

@author: guo
"""
import pandas as pd

dt = pd.read_excel(r'C:\Users\86150\Desktop\0302.xlsx')

seconds_s = 0 
seconds_x = 0

list_s = []
list_x = []
for index,row in dt.iterrows():

    if row['soaWorkFinishType'] == '完成':
         if row['soaTcntrPut'] == 'Y' and len(str(row['soaTcntrPos'])) != 0 and index <= 20:
            h,m,s = str(row['loadS3Time']).split(':')
            seconds_s += int(m)*60+int(s)
            list_s.append(str(row['loadS3Time']))
         elif row['soaTcntrPut'] == 'Y' and len(str(row['soaTcntrPos'])) != 0 and index > 20:
            h,m,s = str(row['loadS3Time']).split(':')
            seconds_x += int(m)*60+int(s)
            list_x.append(str(row['loadS3Time']))
            
print(seconds_s)
print(seconds_x)
print(list_s)
print(list_x)

print(seconds_s/len(list_s))
print(seconds_x/len(list_x))
