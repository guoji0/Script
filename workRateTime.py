# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:08:34 2022

@author: guo
"""
import pandas as pd
from collections import Counter
from time import gmtime
from time import strftime

dt = pd.read_excel(r'C:\Users\86150\Desktop\0217.xlsx')
all_move_list = []
success_move_list = []
success_move_time_dict = {}
csv_heaher = ['日期','作业类型','集卡类型','总数量','成功数','失败数','成功平均时间','成功率']
for index,row in dt.iterrows():
    if row['soaWorkFinishType'] == '完成':
        h,m,s = row['moveTotalTime'].split(':')
        row['moveTotalTime'] = int(m)*60+int(s)
        all_move = str(row['date'])+'&'+str(row['soaWorkType'])+'&'+str(row['soaTruckType'])
        all_move_list.append(all_move)
        if row['soaTcntrGet'] == 'Y' and row['soaTcntrPut'] == 'Y':
            success_move = str(row['date'])+'&'+str(row['soaWorkType'])+'&'+str(row['soaTruckType'])
            success_move_list.append(success_move)
            if success_move in success_move_time_dict.keys():
                success_move_time_dict[success_move].append(row['moveTotalTime'])
            else:
                success_move_time_dict[success_move] = [row['moveTotalTime']]

# print(success_move_time_dict)
for k,v in success_move_time_dict.items():
    success_move_time_dict[k] = strftime('%H:%M:%S',gmtime(int(sum(v)/len(v))))
            

move_num_dict = {}
total_move_dict = {}
all_move_dict = dict(Counter(all_move_list))
success_move_dict = dict(Counter(success_move_list))


def dict_merge(dict1,dict2,dict_new):
    for k1,v1 in dict1.items():
        for k2,v2 in dict2.items():
            if k1 == k2:
                dict_new[k1] = [v1,v2]
            elif k1 not in dict2.keys():
                dict_new[k1] = [v1]
    return(dict_new)
move_num_dict = dict_merge(all_move_dict,success_move_dict,move_num_dict)


total_move_dict = dict_merge(move_num_dict, success_move_time_dict, total_move_dict)
final_list = []

for k,v in total_move_dict.items():
    single_list = []
    date,workType,truckType = k.split('&')
    total = v[0][0]
    if len(v[0]) == 2:
        success = v[0][1]
        failure = int(total) - int(success) 
        avgTime = v[1]
        rate = str(round(float(success/total),2)*100)+'%'
    else:
        success = 0
        failure = total
        avgTime = 0
        rate = 0
    single_list.append(date)
    single_list.append(workType)
    single_list.append(truckType)
    single_list.append(total)
    single_list.append(success)
    single_list.append(failure)
    single_list.append(avgTime)
    single_list.append(rate)
    final_list.append(single_list)
df = pd.DataFrame(final_list)
df.to_excel(r'C:\Users\86150\Desktop\021701.xlsx',header=csv_heaher,index=False)
        
