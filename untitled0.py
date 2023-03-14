# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 09:06:17 2023

@author: guo
"""
import pandas as pd
import numpy as np

data = pd.read_excel(r'C:\Users\86150\Desktop\感知结果与TOS数据对比导出.xlsx')
data.drop(data.tail(1).index,inplace=True)
allWorkType = allWorkTypeCount = {}
WorkCount = VehicleCount = VehicleCountTrue = CntrCount = CntrCountTrue = RowCount = RowCountTrue = 0
for index,row in data.iterrows():
    WorkCount += 1
    HnoWorkType = str(row['实际RTG编号']) + '&' + str(row['操作过程'])
    if HnoWorkType not in allWorkType.keys():
        allWorkType[HnoWorkType] = [0 for i in range(10)]
        allWorkType[HnoWorkType][0] = 1
        if row['RTG感知车号'] is not np.nan:
            allWorkType[HnoWorkType][1] = 1
            VehicleCount += 1
            if row['RTG感知车号'] == row['车号']:
                allWorkType[HnoWorkType][2] = 1
                VehicleCountTrue += 1
            else:
                pass
        if row['RTG感知箱号'] is not np.nan:
            allWorkType[HnoWorkType][4] = 1
            CntrCount += 1
            if row['RTG感知箱号'] == row['箱号']:
                allWorkType[HnoWorkType][5] = 1
                CntrCountTrue += 1
            else:
                pass
        if row['RTG场箱位'] is not np.nan:
            allWorkType[HnoWorkType][7] = 1
            RowCount += 1
            if row['RTG场箱位'] == row['场箱位']:
                allWorkType[HnoWorkType][8] = 1
                RowCountTrue += 1
            else:
                pass
    else:
        allWorkType[HnoWorkType][0] += 1
        if row['RTG感知车号'] is not np.nan:
            allWorkType[HnoWorkType][1] += 1
            VehicleCount += 1
            if row['RTG感知车号'] == row['车号']:
                allWorkType[HnoWorkType][2] += 1
                VehicleCountTrue += 1
            else:
                pass
        if row['RTG感知箱号'] is not np.nan:
            allWorkType[HnoWorkType][4] += 1
            CntrCount += 1
            if row['RTG感知箱号'] == row['箱号']:
                allWorkType[HnoWorkType][5] += 1
                CntrCountTrue += 1
            else:
                pass
        if row['RTG场箱位'] is not np.nan:
            allWorkType[HnoWorkType][7] += 1
            RowCount += 1
            if row['RTG场箱位'] == row['场箱位']:
                allWorkType[HnoWorkType][8] += 1
                RowCountTrue += 1
            else:
                pass
#print(WorkCount ,VehicleCount ,VehicleCountTrue, CntrCount, CntrCountTrue, RowCount,RowCountTrue)
allWorkTypeList = []
for key ,value in allWorkType.items():
    allWorkTypeList.append(key.split('&')+value)
# print(allWorkTypeList)


countWork = {}

for subList in allWorkTypeList:
    if subList[0] not in countWork:
        countWork[subList[0]] = subList[2::]
    else:        
        countWork[subList[0]] = np.sum([countWork[subList[0]],subList[2::]],axis=0).tolist()

for key,value in countWork.items():
    if key != 'nan':
        countWorkList = []
        countWorkList.append(key)
        countWorkList += (['小计']+value)
        allWorkTypeList.append(countWorkList)
    else:
        pass

for subList in allWorkTypeList:
    subList[5] = str(round(float(subList[4]/subList[3])*100,2))+'%' if subList[3] != 0 else 0
    subList[8] = str(round(float(subList[7]/subList[6])*100,2))+'%' if subList[6] != 0 else 0
    subList[11] = str(round(float(subList[10]/subList[9])*100,2))+'%' if subList[9] != 0 else 0

SingalCount = ['All','总计'] + [WorkCount ,VehicleCount ,VehicleCountTrue,str(round(float(VehicleCountTrue/VehicleCount)*100,2))+'%', 
                              CntrCount, CntrCountTrue, str(round(float(CntrCountTrue/CntrCount)*100,2))+'%',
                              RowCount,RowCountTrue,str(round(float(RowCountTrue/RowCount)*100,2))+'%']
# SingalCount1 =['All','车-场']+[sum([i[2] for i in allWorkTypeList if '车―场' in i])]
# print(SingalCount1)
allWorkTypeList.append(SingalCount)
# print(allWorkTypeList)
header = ['车号','作业类型','任务数量','车号上报','准确车号上报','车号上报成功率','箱号上报','准确箱号上报','箱号上报成功率','场箱位上报','准确场箱位上报','场箱位成功率']
df = pd.DataFrame(allWorkTypeList)
df = df.sort_values(by=[0,2],ascending=[True,True])

df.to_excel(r'C:\Users\86150\Desktop\感知结果与TOS数据对比导出0314.xlsx',header=header,index=False)
# df.to_excel(r'C:\Users\86150\Desktop\test.xlsx')
