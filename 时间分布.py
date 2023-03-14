import pandas as pd
import numpy as np
import chardet
def PLCError_code(plc):
    plccode_list = []
    for code in plc:
        code = str(code)
        code = code.replace(" ", "nan")
        new_code = code.split('|')
        for i in new_code:
            if i != "" and i != "nan":
                i = int(i)
                if i != 0:
                    plccode_list.append(i)
    codelist = []
    if plccode_list:
        new_plccode_list = list(set(plccode_list))
        number = []
        for item in new_plccode_list:
            num = plccode_list.count(item)
            number.append(num)
        for x, y in zip(new_plccode_list, number):
            x = str(x)
            y = str(y)
            code = x + "(" + y + ")"
            codelist.append(code)
    codelist = ",".join(codelist)
    return codelist
def unloadtime(dsch_data):
    s0 = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s0time = dsch_data[dsch_data['soaTcntrGet'] == 'Y']["unloadS0Time"]
    for time in s0time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s0 += time
    s1time = dsch_data[dsch_data['soaTcntrGet'] == 'Y']["unloadS1Time"]
    for time in s1time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s1 += time
    s2time = dsch_data[dsch_data['soaTcntrGet'] == 'Y']["unloadS2Time"]
    for time in s2time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s2 += time
    s3time = dsch_data[dsch_data['soaTcntrGet'] == 'Y']["unloadS3Time"]
    for time in s3time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s3 += time
    s5time = dsch_data[dsch_data['soaTcntrGet'] == 'Y']["unloadLiftTime"]
    for time in s5time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s5 += time
    success = len(dsch_data[dsch_data['soaTcntrGet'] == 'Y'])
    if success > 0:
        s0 = s0 // success
        s1 = s1 // success
        s2 = s2 // success
        s3 = s3 // success
        s5 = s5 // success
        he = s0 + s1 + s2 + s3 + s4 + s5
    else:
        s0 = "/"
        s1 = "/"
        s2 = "/"
        s3 = "/"
        s4 = "/"
        s5 = "/"
        he = "/"
    return s0,s1,s2,s3,s4,s5,he
def loadtime(dsch_data):
    s0 = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s0time = dsch_data[dsch_data['soaTcntrPut'] == 'Y']["loadS0Time"]
    for time in s0time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s0 += time
    s1time = dsch_data[dsch_data['soaTcntrPut'] == 'Y']["loadS1Time"]
    for time in s1time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s1 += time
    s2time = dsch_data[dsch_data['soaTcntrPut'] == 'Y']["loadS2Time"]
    for time in s2time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s2 += time
    s3time = dsch_data[dsch_data['soaTcntrPut'] == 'Y']["loadS3Time"]
    for time in s3time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s3 += time
    s4time = dsch_data[dsch_data['soaTcntrPut'] == 'Y']["loadS4Time"]
    for time in s4time:
        time = str(time)
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s4 += time
    s5time = dsch_data[dsch_data['soaTcntrPut'] == 'Y']["loadLiftTime"]
    for time in s5time:
        time = str(time)
        if time == 'nan':
            time = 0
        else:            
            time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        s5 += time
    success = len(dsch_data[dsch_data['soaTcntrPut'] == 'Y'])
    if success>0:
        s0 = s0 // success
        s1 = s1 // success
        s2 = s2 // success
        s3 = s3 // success
        s4 = s4 // success
        s5 = s5 // success
        he = s0 + s1 + s2 + s3 + s4 + s5
    else:
        s0 = "/"
        s1 = '/'
        s2 = '/'
        s3 = '/'
        s4 = '/'
        s5 = '/'
        he = '/'
    return s0, s1, s2, s3, s4, s5, he
def Gans3(dsch_data,mac,work_type,j):
    fail_dsch_data = dsch_data[dsch_data['soaTcntrPut'] == 'N']
    plc = (fail_dsch_data["PLCErrorCode"])
    codelist = PLCError_code(plc)
    total = len(dsch_data)
    success = len(dsch_data[dsch_data['soaTcntrPut'] == 'Y'])
    fail = total - success
    success_rate = str(round((success / total) * 100))
    new_success_rate = success_rate + "%"
    s0, s1, s2, s3, s4, s5, he = loadtime(dsch_data)
    result_list = []
    workdata = mac + ';' + str(j) + ';' + work_type + ';' + str(total) + ';' + str(success) + ';' + str(fail) + ';' + \
               new_success_rate + ';' + codelist + ';' + str(s0) + ';' + str(s1) + ';' + str(s2) + ';' + str(s3) + \
               ';' + str(s4) + ';' + str(s5) + ';' + str(he)
    for i in workdata.split(";"):
        result_list.append(i)
    return result_list
def unloadGans3(dsch_data,mac,work_type,j):
    fail_dsch_data = dsch_data[dsch_data['soaTcntrPut'] == 'N']
    plc = (fail_dsch_data["PLCErrorCode"])
    codelist = PLCError_code(plc)
    total = len(dsch_data)
    success = len(dsch_data[dsch_data['soaTcntrPut'] == 'Y'])
    fail = total - success
    success_rate = str(round((success / total) * 100))
    new_success_rate = success_rate + "%"
    s0, s1, s2, s3, s4, s5, he = unloadtime(dsch_data)
    result_list = []
    workdata = mac + ';' + str(j) + ';' + work_type + ';' + str(total) + ';' + str(success) + ';' + str(fail) + ';' + \
               new_success_rate + ';' + codelist + ';' + str(s0) + ';' + str(s1) + ';' + str(s2) + ';' + str(s3) + \
               ';' + str(s4) + ';' + str(s5) + ';' + str(he)
    for i in workdata.split(";"):
        result_list.append(i)
    return result_list
def cntrset(cntr):
    cntlist = []
    for cnt in cntr:
        cnt = cnt[0:4]
        cntlist.append(cnt)
    int_cntlist = []
    for newcnt in cntlist:
        newcnt = int(newcnt)
        int_cntlist.append(newcnt)
    new_cntlist = sorted(list(set(int_cntlist)))
    return new_cntlist
def read_csv(table_path,encodetype):
    data_type = {'soaTcntrPos':np.str,'PLCErrorCode': np.str,'unloadS0Time': np.str,'unloadS1Time': np.str,
                 'unloadS2Time': np.str,'unloadS3Time': np.str,'unloadLiftTime': np.str,'loadS0Time': np.str,
                 'loadS1Time': np.str,'loadS2Time': np.str,'loadS3Time': np.str,'loadS4Time': np.str,
                 'loadLiftTime': np.str,'unloadGanMoveCntS3': np.str,'loadGanMoveCntS3': np.str,'soaScntrPos': np.str}
    data = pd.read_csv(table_path, encoding=encodetype,dtype=data_type)
    cp_data = data[data['soaWorkFinishType'] == '完成']
    data_worktype = cp_data['soaWorkType'].drop_duplicates()
    new_data_worktype = list(data_worktype)
    mac = list(cp_data['machNo'].drop_duplicates())[0]
    work_list = []
    if '翻箱' or '装船' or '提箱' or '转堆提箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['翻箱','装船','提箱','转堆提箱']))]
        cntr = list(dsch_data['soaScntrPos'].drop_duplicates())
        new_cntlist = cntrset(cntr)
        print(new_cntlist)
        for i in new_cntlist:
            if len(dsch_data[dsch_data["soaScntrPos"].str.contains(r'^' + str(i) + '.*')]) > 0:
                unload_data = dsch_data[dsch_data["soaScntrPos"].str.contains(r'^'+str(i)+'.*')]
                work_type = '堆场区抓箱总和'
                result_list = unloadGans3(unload_data, mac, work_type,i)
                work_list.append(result_list)
                if len(unload_data[unload_data["unloadGanMoveCntS3"]=='0']) > 0:
                    dsch_data1 = unload_data[unload_data["unloadGanMoveCntS3"]=='0']
                    work_type = '堆场区抓箱未动大车'
                    result_list = unloadGans3(dsch_data1, mac, work_type,i)
                    work_list.append(result_list)
                if len(unload_data[(unload_data["unloadGanMoveCntS3"]!='0') & (unload_data["unloadGanDistS3"] < 0)]) > 0:
                    dsch_data2 = unload_data[(unload_data["unloadGanMoveCntS3"]!='0') & (unload_data["unloadGanDistS3"] < 0)]
                    work_type = '堆场区抓箱向左动大车'
                    result_list = unloadGans3(dsch_data2, mac, work_type,i)
                    work_list.append(result_list)
                if len(unload_data[(unload_data["unloadGanMoveCntS3"]!='0') & (unload_data["unloadGanDistS3"] > 0)]) > 0:
                    dsch_data3 = unload_data[(unload_data["unloadGanMoveCntS3"]!='0') & (unload_data["unloadGanDistS3"] > 0)]
                    work_type = '堆场区抓箱向右动大车'
                    result_list = unloadGans3(dsch_data3, mac, work_type,i)
                    work_list.append(result_list)
    df = pd.DataFrame(data=work_list,columns=['车号',"贝位",'作业类型','作业次数','成功','失败',
                                          '自动化比例','PLCErrorcode',"0阶段平均时长","一阶段平均时长","二阶段平均时长",
                                          "三阶段平均时长",'四阶段平均时长',"lift阶段平均时长","总时长"])
    return df
def read_csv2(table_path,encodetype):
    data_type = {'soaTcntrPos':np.str,'PLCErrorCode': np.str,'unloadS0Time': np.str,'unloadS1Time': np.str,
                 'unloadS2Time': np.str,'unloadS3Time': np.str,'unloadLiftTime': np.str,'loadS0Time': np.str,
                 'loadS1Time': np.str,'loadS2Time': np.str,'loadS3Time': np.str,'loadS4Time': np.str,
                 'loadLiftTime': np.str,'unloadGanMoveCntS3': np.str,'loadGanMoveCntS3': np.str,'soaScntrPos': np.str}
    data = pd.read_csv(table_path, encoding=encodetype,dtype=data_type)
    cp_data = data[data['soaWorkFinishType'] == '完成']
    data_worktype = cp_data['soaWorkType'].drop_duplicates()
    new_data_worktype = list(data_worktype)
    mac = list(cp_data['machNo'].drop_duplicates())[0]
    work_list = []
    if '翻箱' or '卸船' or '进箱' or '转堆进箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['翻箱', '卸船', '进箱', '转堆进箱']))]
        cntr = list(dsch_data['soaTcntrPos'].drop_duplicates())
        new_cntlist = cntrset(cntr)
        if len(dsch_data[dsch_data["soaTcntrPos"].str.contains(r'.*?[234]\b')]) > 0:
            dsch_data = dsch_data[dsch_data["soaTcntrPos"].str.contains(r'.*?[234]\b')]
            for i in new_cntlist:
                if len(dsch_data[dsch_data["soaTcntrPos"].str.contains(r'^' + str(i) + '.*')]) > 0:
                    load_data = dsch_data[dsch_data["soaTcntrPos"].str.contains(r'^' + str(i) + '.*')]
                    work_type = '堆场区叠箱总和'
                    result_list = Gans3(load_data,mac,work_type,i)
                    work_list.append(result_list)
                    if len(load_data[load_data["loadGanMoveCntS3"]=='0']) > 0:
                        dsch_data1 = load_data[load_data["loadGanMoveCntS3"]=='0']
                        work_type = '堆场区叠箱未动大车'
                        result_list = Gans3(dsch_data1, mac, work_type,i)
                        work_list.append(result_list)
                        # len(it_dsch_data[(it_dsch_data['soaTcntrGet'] == 'Y') & (it_dsch_data['soaTcntrPut'] == 'Y')])
                    if len(load_data[(load_data["loadGanMoveCntS3"]!='0') & (load_data["loadGanDistS3"] < 0)]) > 0:
                        dsch_data2 = load_data[(load_data["loadGanMoveCntS3"]!='0') & (load_data["loadGanDistS3"] < 0)]
                        work_type = '堆场区叠箱向左动大车'
                        result_list = Gans3(dsch_data2, mac, work_type,i)
                        work_list.append(result_list)
                    if len(load_data[(load_data["loadGanMoveCntS3"]!='0') & (load_data["loadGanDistS3"] > 0)]) > 0:
                        dsch_data3 = load_data[(load_data["loadGanMoveCntS3"]!='0') & (load_data["loadGanDistS3"] > 0)]
                        work_type = '堆场区叠箱向右动大车'
                        result_list = Gans3(dsch_data3, mac, work_type,i)
                        work_list.append(result_list)
    df = pd.DataFrame(data=work_list,columns=['车号',"贝位",'作业类型','作业次数','成功','失败',
                                              '自动化比例','PLCErrorcode',"0阶段平均时长","一阶段平均时长","二阶段平均时长",
                                              "三阶段平均时长",'四阶段平均时长',"lift阶段平均时长","总时长"])
    return df
def main():
    table_path = r"C:\Users\86150\Desktop\csv0408.csv"
    output_path = r"C:\Users\86150\Desktop\时间分布.xlsx"
    writter = pd.ExcelWriter(output_path)
    f = open(table_path, "rb")
    data = f.read()
    encodetype = chardet.detect(data)["encoding"]
    df1 = read_csv(table_path,encodetype)
    df2 = read_csv2(table_path,encodetype)
    df1.to_excel(writter, index=False, sheet_name="抓箱时间分布统计")
    df2.to_excel(writter,index=False,sheet_name="叠箱时间分布统计")
    writter.save()
if __name__ == '__main__':
    main()
