# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:04:57 2022

@author: guo
"""
import pandas as pd
import math 
from collections import Counter
dt = pd.read_excel(r'C:\Users\86150\Desktop\0218.xlsx')
csv_header = ['日期','作业类型','总数量','成功数','失败数','成功率','IPCErrCode','PLCErrCode']
getType = []
putType = []
getErrCodeALL = []
putErrCodeALL = []
dt = dt[dt['soaWorkFinishType'] =='完成'].reset_index(drop=True)
for index,row in dt.iterrows():
    if math.isnan(row['soaScntrPos']):
        row['soaScntrPos'] = ''
    else:
        row['soaScntrPos'] = str(int(row['soaScntrPos']))
    if math.isnan(row['soaTcntrPos']):
        row['soaTcntrPos'] = ''
    else:
        row['soaTcntrPos'] = str(int(row['soaTcntrPos']))        
    
    if len(row['soaScntrPos']) == 6 and row['soaTruckType'] == '内集卡':
        getType.append('堆场抓箱')
        putType.append('内集卡放箱')
    elif len(row['soaScntrPos']) == 6 and  row['soaTruckType'] == 'AIV':
        getType.append('堆场抓箱')
        putType.append('内集卡放箱')
    elif len(row['soaScntrPos']) == 6 and  row['soaTruckType'] == '外集卡':
        getType.append('堆场抓箱')
        putType.append('外集卡放箱')
    elif len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] == '1' and len(row['soaScntrPos']) == 6:
        getType.append('堆场抓箱')
        putType.append('堆场首层')
    elif len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1' and len(row['soaScntrPos']) == 6:
        getType.append('堆场抓箱')
        putType.append('堆场叠箱')        
    elif len(row['soaScntrPos']) == 0 and  row['soaTruckType'] == 'AIV' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1':
        putType.append('堆场叠箱') 
        getType.append('内集卡抓箱')
    elif len(row['soaScntrPos']) == 0 and  row['soaTruckType'] == 'AIV' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] == '1':
        putType.append('堆场首层') 
        getType.append('内集卡抓箱')
    elif len(row['soaScntrPos']) == 0 and  row['soaTruckType'] == '内集卡' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1':
        putType.append('堆场叠箱')
        getType.append('内集卡抓箱')
    elif len(row['soaScntrPos']) == 0 and  row['soaTruckType'] == '内集卡' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] == '1':
        putType.append('堆场首层')
        getType.append('内集卡抓箱')
    elif len(row['soaScntrPos']) == 0 and  row['soaTruckType'] == '外集卡' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] != '1':
        putType.append('堆场叠箱')
        getType.append('外集卡抓箱')
    elif len(row['soaScntrPos']) == 0 and  row['soaTruckType'] == '外集卡' and len(row['soaTcntrPos']) == 6 and row['soaTcntrPos'][-1] == '1':
        putType.append('堆场首层')
        getType.append('外集卡抓箱')
    else:
        
        putType.append('NULL')
        getType.append('NULL')
        
        
    getErrCodeList = []
    putErrCodeList = []
    if len(row['PLCErrorCode']) >= 3:
        
        getPLCErrCode = row['PLCErrorCode'].split('|')[0]
        putPLCErrCode = row['PLCErrorCode'].split('|')[1]
    else:
        getPLCErrCode = ['0']
        putPLCErrCode = ['0']
    
    getIPCErrCodeList = str(row['IPCErrorCodeStr']).split(',')[0].split('|')
    putIPCErrCodeList = str(row['IPCErrorCodeStr']).split(',')[-1].split('|')


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

df_getErrCodeALL = pd.DataFrame({'getErrCodeALL':getErrCodeALL})
df_putErrCodeALL = pd.DataFrame({'putErrCodeALL':putErrCodeALL})   

df_getType = pd.DataFrame(getType,columns=['getType'])
df_putType = pd.DataFrame(putType,columns=['putType'])
dt = pd.concat([dt,df_getType,df_putType,df_getErrCodeALL,df_putErrCodeALL],axis=1)
# print(dt['soaTcntrGet'])
# print(dt['soaTcntrPut'])

resultGet = []
resultPut = []
resultSuccessGet = []
resultSuccessPut = []
GetErrCode = []
PutErrCode = []
for index,row in dt.iterrows():
    resultGet.append(row['date']+'&'+row['getType'])
    resultPut.append(row['date']+'&'+row['putType'])
    if row['soaTcntrGet'] == 'Y':

        resultSuccessGet.append(row['date']+'&'+row['getType'])
    else:
        for i in row['getErrCodeALL']:
              GetErrCode.append(row['date']+'&'+row['getType']+'&&'+i)
    if row['soaTcntrPut'] == 'Y':

        resultSuccessPut.append(row['date']+'&'+row['putType'])
    else:
        for i in row['putErrCodeALL']:
              PutErrCode.append(row['date']+'&'+row['putType']+'&&'+i)

        
        
# print(GetErrCode)    
# print(PutErrCode)    
# print(resultGet)
# print(resultPut)
# print(resultSuccessGet)
# print(resultSuccessPut)

resultGetdict = dict(Counter(resultGet))
resultPutdict = dict(Counter(resultPut))
resultSuccessGetdict = dict(Counter(resultSuccessGet))
resultSuccessPutdict = dict(Counter(resultSuccessPut))
# print(resultGetdict)
# print(resultPutdict)
# print(resultSuccessGetdict)
# print(resultSuccessPutdict)

def dict_merge(dict1,dict2,dict_new):
    for k1,v1 in dict1.items():
        for k2,v2 in dict2.items():
            if k1 == k2:
                dict_new[k1] = [v1,v2]
            elif k1 not in dict2.keys():
                dict_new[k1] = [v1]
    return(dict_new)

GetDict = {}
PutDict = {}
dict_merge(resultGetdict,resultSuccessGetdict,GetDict)
dict_merge(resultPutdict,resultSuccessPutdict,PutDict)

GetErrCodeDict = dict(Counter(GetErrCode))
PutErrCodeDict = dict(Counter(PutErrCode))
# print(GetErrCodeDict)
# print(PutErrCodeDict)

def DictHandle(dict1,dict2):
    for k,v in dict1.items():
        if k.split('&&')[0] not in dict2.keys():
            dict2[k.split('&&')[0]] = k.split('&&')[1]+'('+str(v)+')'+ ' '
        else:
            dict2[k.split('&&')[0]] += k.split('&&')[1]+'('+str(v)+')'+' '
    return(dict2)
GetErrCodeDictLast = {}
DictHandle(GetErrCodeDict,GetErrCodeDictLast)
# print(GetErrCodeDictLast)

PutErrCodeDictLast = {}
DictHandle(PutErrCodeDict,PutErrCodeDictLast)
# print(PutErrCodeDictLast)

GetDictLast = {}
PutDictLast = {}
dict_merge(GetDict,GetErrCodeDictLast,GetDictLast)
dict_merge(PutDict,PutErrCodeDictLast,PutDictLast)
# print(GetDictLast)
# print(PutDictLast)
LastDict = dict(GetDictLast,**PutDictLast)
# print(LastDict)
LastList = []
for k,v in LastDict.items():
    alist = []
    IPCErrCode = ''
    PLCErrCode = ''
    date = k.split('&')[0]
    workType = k.split('&')[1]
    total = v[0][0]
    if len(v[0]) == 2:
        success = v[0][1]
        failure = int(total) - int(success)
        rate = str(round(float(success/total),2)*100)+'%'
        if v[0][0] == v[0][1]:
            IPCErrCode = ''
            PLCErrCode = ''
        else:
            for i in  v[1].rstrip().split(' '):
                if len(i) == 7:
                    print(1)
                    IPCErrCode += i + ','
                else:
                    PLCErrCode += i + ','
            
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
    IPCErrCode = ''
    PLCErrCode = ''
    LastList.append(alist)
# print(LastList)
df = pd.DataFrame(LastList)
# print(df)
df.to_excel(r'C:\Users\86150\Desktop\021815.xlsx',header=csv_header,index=False)
