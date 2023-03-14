# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:26:44 2022

@author: guo
"""
import pandas as pd

from collections import Counter
from openpyxl import load_workbook
data = pd.read_excel(r'C:\Users\86150\Desktop\0331.xlsx')
data['soaTcntrPos'].fillna('0',inplace=True)
load_header = ['贝位','作业个数','作业点动次数','初定位偏左','初定位偏右','点动占比','偏左占比','偏右占比']
bay_list = []
left_list = []
right_list = []
dict1 = {}
dict_final = {}
final_list = []
for index,row in data.iterrows():
    if row['soaWorkFinishType'] == '完成':
        row['soaTcntrPos'] = str(int(row['soaTcntrPos']))
        if len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1':
            bay = str(row['soaTcntrPos'])[2:4]
            bay_list.append(bay)
            if row['loadGanMoveCntS3'] != 0 and row['loadGanDistS3'] < 0:
                right_list.append(bay + 'R')
            elif row['loadGanMoveCntS3'] != 0 and row['loadGanDistS3'] > 0:
                left_list.append(bay + 'L')
            else:
                pass
        else:
            pass
        

                        
# print(bay_list)
# print(left_list)
# print(right_list)

bay_dict = dict(Counter(bay_list))
left_dict = dict(Counter(left_list))
right_dict = dict(Counter(right_list))
left_dict1 = {}
right_dict1 = {}
for k,v in left_dict.items():
    left_dict1[k[0:2]] = k[-1] + str(v)

for k,v in right_dict.items():
    right_dict1[k[0:2]] = k[-1] + str(v)

print(bay_dict)
print(left_dict1)
print(right_dict1)


def dict_merge(dict1,dict2,dict_new):
    for k1,v1 in dict1.items():    
        if k1 in dict2.keys():
            dict_new[k1] = [v1,dict2[k1]]
        elif k1 not in dict2.keys():
            dict_new[k1] = [v1]
    for k2,v2 in dict2.items():
        if k2 in dict_new.keys():
          pass
        else:
            dict_new[k2] = [v2]
            
    return(dict_new)

dict1 = dict_merge(left_dict1,right_dict1,dict1)
print(dict1)
dict_final = dict_merge(bay_dict,dict1,dict_final)
print(dict_final)

for k,v in dict_final.items():
    alist = []
    bay = k
    bay_num = v[0]
    if len(v) == 1:
        bay_left = 0
        bay_right = 0
    elif len(v) != 1:
        if len(v[1]) == 1 and 'L' in v[1][0]:
            bay_left = int(v[1][0][-1])
            bay_right = 0
        elif len(v[1]) == 1 and 'R' in v[1][0]:
            bay_left = 0
            bay_right = int(v[1][0][-1])
        elif len(v[1][1]) == 2:
            bay_left = int(v[1][0][-1])
            bay_right = int(v[1][1][-1])
    move_num = bay_left + bay_right
    move_rate = str(round(float(move_num/bay_num)*100,2))+'%'
    left_rate = str(round(float(bay_left/bay_num)*100,2))+'%'
    right_rate = str(round(float(bay_right/bay_num)*100,2))+'%'
    alist.append(bay)
    alist.append(bay_num)    
    alist.append(move_num)
    alist.append(bay_left)
    alist.append(bay_right)
    alist.append(move_rate)
    alist.append(left_rate)
    alist.append(right_rate)
    final_list.append(alist)
df_move = pd.DataFrame(final_list)

book = load_workbook(r'C:\Users\86150\Desktop\0331.xlsx')
writer = pd.ExcelWriter(r'C:\Users\86150\Desktop\0331.xlsx', engine='openpyxl')
writer.book = book
df_move.to_excel(writer,header=load_header,sheet_name='move',index=False,engine='xlsx')
writer.save()
writer.close()
