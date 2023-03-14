# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:13:48 2022

@author: guo
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 10:53:52 2022

@author: guo
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:08:34 2022

@author: guo
"""
import pandas as pd
from collections import Counter
from time import gmtime
from time import strftime
from openpyxl import load_workbook


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


def DictHandle(dict1,dict2):
    for k,v in dict1.items():
        if k.split('&&')[0] not in dict2.keys():
            dict2[k.split('&&')[0]] = k.split('&&')[1]+'('+str(v)+')'+ ' '
        else:
            dict2[k.split('&&')[0]] += k.split('&&')[1]+'('+str(v)+')'+' '
    return(dict2)
print('**************************')
source_file = input('请输入您要处理的文件名:')
print('**************************')
print('处理完成!')





dt = pd.read_excel(source_file)
# dt = pd.read_excel(r'C:\Users\86150\Desktop\0216.xlsx')

all_move_list = []
success_move_list = []
LCPS_move = []
success_move_time_dict = {}

getType = []
putType = []
getErrCodeALL = []
putErrCodeALL = []

sheet_name1 = 'work_rate'
sheet_name2 = 'work_failure'
sheet_name3 = 'work_move'
rate_header = ['日期','RTG编号','作业类型','集卡类型','总数量','成功数','失败数','成功平均时间','成功率','防撞次数']
failure_header = ['日期','作业类型','总数量','成功数','失败数','成功率','IPCErrCode','PLCErrCode']
load_header = ['贝位','作业个数','作业点动次数','初定位偏左','初定位偏右','点动占比','偏左占比','偏右占比']
bay_list = []
left_list = []
right_list = []
dict1 = {}
dict_final = {}
final_list = []
dt = dt[dt['soaWorkFinishType'] =='完成'].reset_index(drop=True)
dt['PLCErrorCode'].fillna('0|0',inplace=True)
dt['soaTcntrPos'].fillna('0',inplace=True)
dt['soaScntrPos'].fillna('0',inplace=True)
for index,row in dt.iterrows():
    row['soaTcntrPos'] = str(int(row['soaTcntrPos']))
    row['soaScntrPos'] = str(int(row['soaScntrPos']))
    row['date'] = str(row['date'])
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
    getErrCodeList = []
    putErrCodeList = [] 
    if len(row['PLCErrorCode']) >= 3:
        
        getPLCErrCode = row['PLCErrorCode'].split('|')[0]
        putPLCErrCode = row['PLCErrorCode'].split('|')[1]
    else:
        getPLCErrCode = ['0']
        putPLCErrCode = ['0']
        
    
    getIPCErrCodeList = map(lambda x : x[:4],str(row['IPCErrorCodeStr']).split(',')[0].split('|'))
    putIPCErrCodeList = map(lambda x : x[:4],str(row['IPCErrorCodeStr']).split(',')[-1].split('|'))
    print(getIPCErrCodeList)
    print(putIPCErrCodeList)
    
    h,m,s = str(row['moveTotalTime']).split(':')
    row['moveTotalTime'] = int(m)*60+int(s)

        

    all_move = str(row['date'])+'&'+str(row['soaWorkType'])+'&'+str(row['soaTruckType'])
    all_move_list.append(all_move)
    if '1074' in str(row['IPCErrorCodeStr']) or '1075' in str(row['IPCErrorCodeStr']):
        LCPS_move.append(all_move)
        
        
    if row['soaTcntrGet'] == 'Y' and row['soaTcntrPut'] == 'Y':
        success_move = str(row['date'])+'&'+str(row['soaWorkType'])+'&'+str(row['soaTruckType'])
        success_move_list.append(success_move)
        if success_move in success_move_time_dict.keys():
            success_move_time_dict[success_move].append(row['moveTotalTime'])
        else:
            success_move_time_dict[success_move] = [row['moveTotalTime']]
            
            
    if len(row['soaScntrPos']) == 6 and row['soaTruckType'] == '内集卡' and len(row['soaTcntrPos']) == 1:
        getType.append('堆场抓箱')
        putType.append('内集卡放箱')
    elif len(row['soaScntrPos']) == 6 and  row['soaTruckType'] == 'AIV' and len(row['soaTcntrPos']) == 1:
        getType.append('堆场抓箱')
        putType.append('内集卡放箱')
    elif len(row['soaScntrPos']) == 6 and  row['soaTruckType'] == '外集卡' and len(row['soaTcntrPos']) == 1:
        getType.append('堆场抓箱')
        putType.append('外集卡放箱')
    elif len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] == '1' and len(row['soaScntrPos']) == 6:
        getType.append('堆场抓箱')
        putType.append('堆场首层')
    elif len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1' and len(row['soaScntrPos']) == 6:
        getType.append('堆场抓箱')
        putType.append('堆场叠箱')
    elif len(row['soaScntrPos']) == 1 and  row['soaTruckType'] == 'AIV' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1':
        putType.append('堆场叠箱')
        getType.append('内集卡抓箱')
    elif len(row['soaScntrPos']) == 1 and  row['soaTruckType'] == 'AIV' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] == '1':
        putType.append('堆场首层')
        getType.append('内集卡抓箱')
    elif len(row['soaScntrPos']) == 1 and  row['soaTruckType'] == '内集卡' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1':
        putType.append('堆场叠箱')
        getType.append('内集卡抓箱')
    elif len(row['soaScntrPos']) == 1 and  row['soaTruckType'] == '内集卡' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] == '1':
        putType.append('堆场首层')
        getType.append('内集卡抓箱')
    elif len(row['soaScntrPos']) == 1 and  row['soaTruckType'] == '外集卡' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1':
        putType.append('堆场叠箱')
        getType.append('外集卡抓箱')
    elif len(row['soaScntrPos']) == 1 and  row['soaTruckType'] == '外集卡' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] == '1':
        putType.append('堆场首层')
        getType.append('外集卡抓箱')
    else:
        print(row['soaScntrPos'])
        print(row['soaScntrPos'])
        putType.append('NULL')
        getType.append('NULL')
        



    getErrCodeList.append(getPLCErrCode)
    putErrCodeList.append(putPLCErrCode)
    for i in getIPCErrCodeList:
        if i not in getErrCodeList:
            getErrCodeList.append(i)
            
            
    for i in putIPCErrCodeList:
        if i not in putErrCodeList:
            putErrCodeList.append(i)
            
    
    getErrCodeALL.append([i for i in getErrCodeList if len(i) >= 3 and i != 'nan'])
    putErrCodeALL.append([i for i in putErrCodeList if len(i) >= 3 and i != 'nan'])
# print(LCPS_move)
# print(success_move_time_dict)
# print(all_move_list)
for k,v in success_move_time_dict.items():
    success_move_time_dict[k] = strftime('%H:%M:%S',gmtime(int(sum(v)/len(v))))
    
move_num_dict = {}
total_move_dict = {}

all_move_dict = dict(Counter(all_move_list))
success_move_dict = dict(Counter(success_move_list))
LCPS_move_dict = dict(Counter(LCPS_move))
move_num_dict = dict_merge(all_move_dict,success_move_dict,move_num_dict)
total_move_dict = dict_merge(move_num_dict, success_move_time_dict, total_move_dict)
total_move_dict = dict_merge(total_move_dict, LCPS_move_dict, total_move_dict)
# print(total_move_dict)

# print(total_move_dict)
# print(move_num_dict)
final_list_rate = []

for k,v in total_move_dict.items():
    single_list = []
    date,workType,truckType = k.split('&')
    total = v[0][0][0]
    if len(v[0][0]) == 2:
        success = v[0][0][1]
        failure = int(total) - int(success) 
        avgTime = v[0][1]
        rate = str(round(float(success/total)*100,2))+'%'
    else:
        success = 0
        failure = total
        avgTime = 0
        rate = 0
    if len(v) == 2:
        lcps_num = v[1]
    else:
        lcps_num = 0
    single_list.append(date)
    single_list.append(dt['machNo'].iloc[0])
    single_list.append(workType)
    single_list.append(truckType)
    single_list.append(total)
    single_list.append(success)
    single_list.append(failure)
    single_list.append(avgTime)
    single_list.append(rate)
    single_list.append(lcps_num)
    final_list_rate.append(single_list)
# print(final_list_rate)
bay_dict = dict(Counter(bay_list))
left_dict = dict(Counter(left_list))
right_dict = dict(Counter(right_list))
left_dict1 = {}
right_dict1 = {}
for k,v in left_dict.items():
    left_dict1[k[0:2]] = k[-1] + str(v)

for k,v in right_dict.items():
    right_dict1[k[0:2]] = k[-1] + str(v)
dict1 = dict_merge(left_dict1,right_dict1,dict1)
dict_final = dict_merge(bay_dict,dict1,dict_final)


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

    

    

    
df_getErrCodeALL = pd.DataFrame({'getErrCodeALL':getErrCodeALL})
df_putErrCodeALL = pd.DataFrame({'putErrCodeALL':putErrCodeALL})   

df_getType = pd.DataFrame(getType,columns=['getType'])
df_putType = pd.DataFrame(putType,columns=['putType'])
dt = pd.concat([dt,df_getType,df_putType,df_getErrCodeALL,df_putErrCodeALL],axis=1)

resultGet = []
resultPut = []
resultSuccessGet = []
resultSuccessPut = []
GetErrCode = []
PutErrCode = []
for index,row in dt.iterrows():
    resultGet.append(str(row['date'])+'&'+row['getType'])
    resultPut.append(str(row['date'])+'&'+row['putType'])
    if row['soaTcntrGet'] == 'Y':

        resultSuccessGet.append(str(row['date'])+'&'+row['getType'])
    else:
        for i in row['getErrCodeALL']:
              GetErrCode.append(str(row['date'])+'&'+row['getType']+'&&'+i)
    if row['soaTcntrPut'] == 'Y':

        resultSuccessPut.append(str(row['date'])+'&'+row['putType'])
    else:
        for i in row['putErrCodeALL']:
              PutErrCode.append(str(row['date'])+'&'+row['putType']+'&&'+i)
              
resultGetdict = dict(Counter(resultGet))
resultPutdict = dict(Counter(resultPut))
resultSuccessGetdict = dict(Counter(resultSuccessGet))
resultSuccessPutdict = dict(Counter(resultSuccessPut))

GetDict = {}
PutDict = {}
dict_merge(resultGetdict,resultSuccessGetdict,GetDict)
dict_merge(resultPutdict,resultSuccessPutdict,PutDict)

GetErrCodeDict = dict(Counter(GetErrCode))
# print(GetErrCodeDict)
PutErrCodeDict = dict(Counter(PutErrCode))

GetErrCodeDictLast = {}
DictHandle(GetErrCodeDict,GetErrCodeDictLast)
# print(GetErrCodeDictLast)

PutErrCodeDictLast = {}
DictHandle(PutErrCodeDict,PutErrCodeDictLast)


GetDictLast = {}
PutDictLast = {}
dict_merge(GetDict,GetErrCodeDictLast,GetDictLast)
dict_merge(PutDict,PutErrCodeDictLast,PutDictLast)
# print(GetDictLast)
# print(PutDictLast)
LastDict = dict(GetDictLast,**PutDictLast)
# print(LastDict)
# print(LastDict)
LastList = []
for k,v in LastDict.items():
    alist = []
    date = k.split('&')[0]
    workType = k.split('&')[1]
    total = v[0][0]
    IPCErrCode = ''
    PLCErrCode = ''
    if len(v[0]) == 2:
        success = v[0][1]
        failure = int(total) - int(success)
        rate = str(round(float(success/total)*100,2))+'%'
        if v[0][0] == v[0][1]:
            IPCErrCode = ''
            PLCErrCode = ''
        else:
            if len(v) == 2:
                
                for i in  v[1].rstrip().split(' '):
                    if len(i) == 7:
                        IPCErrCode += i + ','
                    else:
                        PLCErrCode += i + ','
            else:
                IPCErrCode = ''
                PLCErrCode = ''
            
    else:
        success = 0
        failure = total
        rate = 0
        
    alist.append(date)
    alist.append(workType)
    alist.append(total)
    alist.append(success)
    alist.append(failure)
    alist.append(rate)
    alist.append(IPCErrCode[:-1])
    alist.append(PLCErrCode[:-1])

    LastList.append(alist)

df_rate = pd.DataFrame(final_list_rate)
df_failure = pd.DataFrame(LastList)
# df_move = pd.DataFrame(final_list)
book = load_workbook(source_file)
writer = pd.ExcelWriter(source_file, engine='openpyxl')
writer.book = book
df_rate.to_excel(writer,header=rate_header,sheet_name=sheet_name1,index=False,engine='xlsx')
df_failure.to_excel(writer,header=failure_header,sheet_name=sheet_name2,index=False,engine='xlsx')
# df_move.to_excel(writer,header=load_header,sheet_name=sheet_name3,index=False,engine='xlsx')
writer.save()
writer.close()
# print('文件已经分别保存到%s的%s,%s,%s中' % (source_file,sheet_name1,sheet_name2,sheet_name3))
print('文件已经分别保存到%s的%s,%s中' % (source_file,sheet_name1,sheet_name2))