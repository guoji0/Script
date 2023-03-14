import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chardet
import datetime
def read_csvdata1(dsch_data,it_dsch_data,mac):
    total = len(it_dsch_data)
    successdata = it_dsch_data[(it_dsch_data['soaTcntrGet'] == 'Y') & (it_dsch_data['soaTcntrPut'] == 'Y')]
    hc = len(successdata[successdata['hoistAntiC']=='Y'])
    success = len(successdata)
    fail = total - success
    success_rate = str(round((success / total) * 100))
    new_success_rate = success_rate + "%"
    average_time = it_dsch_data[(it_dsch_data['soaTcntrGet'] == 'Y') & (it_dsch_data['soaTcntrPut'] == 'Y')]['moveTotalTime']
    total_time = 0
    for time in average_time:
        time = (int(time.split(":")[1])) * 60 + (int(time.split(":")[2]))
        total_time += time
    result_list = []
    if total_time == 0:
        new_total_time = total_time
        work_type = list(dsch_data['soaWorkType'].drop_duplicates())[0]
        work_truck_type = list(it_dsch_data['soaTruckType'].drop_duplicates())[0]
        date = list(dsch_data['date'].drop_duplicates())[0]
        result_list.append(date)
        result_list.append(mac)
        result_list.append(work_type)
        result_list.append(work_truck_type)
        result_list.append(total)
        result_list.append(success)
        result_list.append(fail)
        result_list.append(new_success_rate)
        result_list.append(new_total_time)
        result_list.append(hc)
    else:
        total_time = total_time / success
        new_total_time = "%d:%d:%d" % (total_time // 3600, total_time % 3600 // 60, total_time % 60)
        new_total_time = datetime.datetime.strptime(new_total_time, "%H:%M:%S").time()
        work_type = list(dsch_data['soaWorkType'].drop_duplicates())[0]
        work_truck_type = list(it_dsch_data['soaTruckType'].drop_duplicates())[0]
        date = list(dsch_data['date'].drop_duplicates())[0]
        result_list.append(date)
        result_list.append(mac)
        result_list.append(work_type)
        result_list.append(work_truck_type)
        result_list.append(total)
        result_list.append(success)
        result_list.append(fail)
        result_list.append(new_success_rate)
        result_list.append(new_total_time)
        result_list.append(hc)
    return result_list
def read_csv(table_path,type):
    data = pd.read_csv(table_path,encoding=type,usecols=["date","machNo","soaWorkType","soaWorkFinishType",
                                                          "soaTruckType","soaTcntrGet","soaTcntrPut",
                                                          "moveTotalTime",'hoistAntiC'])
    cp_data = data[data['soaWorkFinishType']=='完成']
    data_worktype = cp_data['soaWorkType'].drop_duplicates()
    new_data_worktype = list(data_worktype)
    work_list = []
    mac = list(cp_data['machNo'].drop_duplicates())[0]
    if '卸船' in new_data_worktype:
        dsch_data = cp_data[cp_data['soaWorkType']=='卸船']
        data_trucktype = dsch_data['soaTruckType'].drop_duplicates()
        new_data_trucktype = list(data_trucktype)
        if '内集卡' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='内集卡']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
        if 'AIV' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='AIV']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
    if '装船' in new_data_worktype:
        dsch_data = cp_data[cp_data['soaWorkType']=='装船']
        data_trucktype = dsch_data['soaTruckType'].drop_duplicates()
        new_data_trucktype = list(data_trucktype)
        if '内集卡' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='内集卡']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
        if 'AIV' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='AIV']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
    if '转堆提箱' in new_data_worktype:
        dsch_data = cp_data[cp_data['soaWorkType']=='转堆提箱']
        data_trucktype = dsch_data['soaTruckType'].drop_duplicates()
        new_data_trucktype = list(data_trucktype)
        if '内集卡' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='内集卡']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
        if 'AIV' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='AIV']
            result_list = read_csvdata1(dsch_data,it_dsch_data, mac)
            work_list.append(result_list)
    if '转堆进箱' in new_data_worktype:
        dsch_data = cp_data[cp_data['soaWorkType']=='转堆进箱']
        data_trucktype = dsch_data['soaTruckType'].drop_duplicates()
        new_data_trucktype = list(data_trucktype)
        if '内集卡' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='内集卡']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
        if 'AIV' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='AIV']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
    if '提箱' in new_data_worktype:
        dsch_data = cp_data[cp_data['soaWorkType']=='提箱']
        data_trucktype = dsch_data['soaTruckType'].drop_duplicates()
        new_data_trucktype = list(data_trucktype)
        if '外集卡' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='外集卡']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
    if '进箱' in new_data_worktype:
        dsch_data = cp_data[cp_data['soaWorkType']=='进箱']
        data_trucktype = dsch_data['soaTruckType'].drop_duplicates()
        new_data_trucktype = list(data_trucktype)
        if '外集卡' in new_data_trucktype:
            it_dsch_data = dsch_data[dsch_data['soaTruckType']=='外集卡']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
    if '翻箱' in new_data_worktype:
        dsch_data = cp_data[cp_data['soaWorkType'] == '翻箱']
        if len(dsch_data)>0:
            it_dsch_data = cp_data[cp_data['soaWorkType']=='翻箱']
            result_list = read_csvdata1(dsch_data,it_dsch_data,mac)
            work_list.append(result_list)
    df = pd.DataFrame(data=work_list,columns=["作业日期","车号","作业类型","集卡类型","作业次数"
                                                ,"成功","失败","自动化比例","平均时间","防撞次数"])
    print(df)
    return df
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
def Gans3(dsch_data,mac,work_type):
    fail_dsch_data = dsch_data[dsch_data['soaTcntrGet'] == 'N']
    plc = (fail_dsch_data["PLCErrorCode"])
    codelist = PLCError_code(plc)
    total = len(dsch_data)
    success = len(dsch_data[dsch_data['soaTcntrGet'] == 'Y'])
    fail = total - success
    success_rate = str(round((success / total) * 100))
    new_success_rate = success_rate + "%"
    result_list = []
    date = list(dsch_data['date'].drop_duplicates())[0]
    workdata = date + ';' + mac + ';' + work_type + ';' + str(total) + ';' + str(success) + ';' + str(fail) + ';' + \
               new_success_rate + ';' + codelist
    for i in workdata.split(";"):
        result_list.append(i)
    return result_list
def read_csv2(table_path,type):
    data_type = {'soaTcntrPos':np.str,'PLCErrorCode': np.str}
    data = pd.read_csv(table_path, encoding=type, usecols=["date","machNo", "soaWorkType", "soaWorkFinishType",
                                                            "soaTruckType","soaTcntrPos", "soaTcntrGet", "soaTcntrPut","PLCErrorCode"],dtype=data_type)
    cp_data = data[data['soaWorkFinishType'] == '完成']
    data_worktype = cp_data['soaWorkType'].drop_duplicates()
    new_data_worktype = list(data_worktype)
    mac = list(cp_data['machNo'].drop_duplicates())[0]
    work_list = []
    if '翻箱' or '装船' or '提箱' or '转堆提箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['翻箱','装船','提箱','转堆提箱']))]
        work_type = '堆场区抓箱'
        result_list = Gans3(dsch_data,mac,work_type)
        work_list.append(result_list)
    if '翻箱' or '卸船' or '进箱' or '转堆进箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['翻箱', '卸船', '进箱', '转堆进箱']))]
        if len(dsch_data[dsch_data["soaTcntrPos"].str.contains(r'.*?[234]\b')]) > 0:
            dsch_data = dsch_data[dsch_data["soaTcntrPos"].str.contains(r'.*?[234]\b')]
            work_type = '堆场区叠箱'
            result_list = Gans3(dsch_data,mac,work_type)
            work_list.append(result_list)
    if '翻箱' or '卸船' or '进箱' or '转堆进箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['翻箱', '卸船', '进箱', '转堆进箱']))]
        if len(dsch_data[dsch_data["soaTcntrPos"].str.contains(r'.*?1\b')]) > 0:
            dsch_data = dsch_data[dsch_data["soaTcntrPos"].str.contains(r'.*?1\b')]
            work_type = '堆场首层箱'
            result_list = Gans3(dsch_data, mac, work_type)
            work_list.append(result_list)
    if '卸船'or '转堆进箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['卸船','转堆进箱']))]
        if len(dsch_data[dsch_data["soaTruckType"]=="内集卡"]) > 0:
            dsch_data = dsch_data[dsch_data["soaTruckType"]=="内集卡"]
            work_type = '内集卡抓箱'
            result_list = Gans3(dsch_data, mac, work_type)
            work_list.append(result_list)
    if '装船'or '转堆提箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['装船','转堆提箱']))]
        if len(dsch_data[dsch_data["soaTruckType"]=="内集卡"]) > 0:
            dsch_data = dsch_data[dsch_data["soaTruckType"]=="内集卡"]
            work_type = '内集卡放箱'
            result_list = Gans3(dsch_data, mac, work_type)
            work_list.append(result_list)
    if '卸船'or '转堆进箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['卸船','转堆进箱']))]
        if len(dsch_data[dsch_data["soaTruckType"]=="AIV"]) > 0:
            dsch_data = dsch_data[dsch_data["soaTruckType"]=="AIV"]
            work_type = 'AIV抓箱'
            result_list = Gans3(dsch_data, mac, work_type)
            work_list.append(result_list)
    if '装船'or '转堆提箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['装船','转堆提箱']))]
        if len(dsch_data[dsch_data["soaTruckType"]=="AIV"]) > 0:
            dsch_data = dsch_data[dsch_data["soaTruckType"]=="AIV"]
            work_type = 'AIV放箱'
            result_list = Gans3(dsch_data, mac, work_type)
            work_list.append(result_list)
    if '进箱'in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['进箱']))]
        if len(dsch_data[dsch_data["soaTruckType"]=="外集卡"]) > 0:
            dsch_data = dsch_data[dsch_data["soaTruckType"]=="外集卡"]
            work_type = '外集卡抓箱'
            result_list = Gans3(dsch_data, mac, work_type)
            work_list.append(result_list)
    if '提箱' in new_data_worktype:
        dsch_data = cp_data[(cp_data['soaWorkType'].isin(['提箱']))]
        if len(dsch_data[dsch_data["soaTruckType"]=="外集卡"]) > 0:
            dsch_data = dsch_data[dsch_data["soaTruckType"]=="外集卡"]
            work_type = '外集卡放箱'
            result_list = Gans3(dsch_data, mac, work_type)
            work_list.append(result_list)
    df = pd.DataFrame(data=work_list,columns=['作业日期',"车号",'作业类型','作业次数','成功','失败','自动化比例','PLCErrorcode'])
    # print(df)
    return df
def Histogram(table_path,img_path,type):
    data_type = {'PLCErrorCode': np.str,'IPCErrorCodeStr': np.str}
    data = pd.read_csv(table_path, encoding=type, usecols=["date","soaWorkFinishType","soaTcntrGet","soaTcntrPut","PLCErrorCode","IPCErrorCodeStr"],dtype=data_type)
    cp_data = data[data['soaWorkFinishType'] == '完成']
    # no_data = cp_data[(data["soaTcntrGet"] == 'N') & (data["soaTcntrPut"] == 'N')]
    # no_data1 = cp_data[(data["soaTcntrGet"] == 'N') & (data["soaTcntrPut"] == 'Y')]
    # no_data2 = cp_data[(data["soaTcntrGet"] == 'Y') & (data["soaTcntrPut"] == 'N')]
    plc = (cp_data["PLCErrorCode"])
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
                else:
                    pass
            else:
                pass
    set_plccpde_list = set(plccode_list)
    number = []
    for item in set_plccpde_list:
        num = plccode_list.count(item)
        number.append(num)
    str1 = []
    for x in set_plccpde_list:
        x = str(x)
        str1.append(x)
    str2 = list(number)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # print(str1,str2)
    rects = plt.bar(str1, str2,color=['r','g','b', 'c', 'm', 'y'],width=0.5)
    for rect in rects:
        height = rect.get_height()
        # plt.text(rect.get_x() + rect.get_width() / 2. - 0.25, 1.01 * height, '%s' % int(height),fontsize=15,horizontalalignment='right' )
        plt.text(rect.get_x() + rect.get_width() / 2. - 0, 1 * height, '%s' % int(height), fontsize=15,
                 horizontalalignment='center')
    plt.xticks(str1, size=15)
    plt.yticks(size=15)
    plt.xlabel('Ls (Degree)', fontsize=15)
    plt.title('PLCerrorcode频数分布',fontsize=15)
    plt.xlabel('分类', fontsize=15)
    text = '\n'.join(('数','量'))
    plt.ylabel(text, fontsize=15,rotation='horizontal'
               ,verticalalignment='center')
    plt.savefig(img_path)



    plt.show()
def main():
    table_path = r"C:\Users\86150\Desktop\csv0409.csv"
    output_path = r"C:\Users\86150\Desktop\数据整理.xlsx"
    # img_path = r"D:\test\20220222\PLCerrorcode.png"
    writter = pd.ExcelWriter(output_path)
    f = open(table_path, "rb")
    data = f.read()
    type = chardet.detect(data)["encoding"]
    df1 = read_csv(table_path,type)
    df2 = read_csv2(table_path,type)
    df1.to_excel(writter,index=False,sheet_name="作业效率")
    df2.to_excel(writter,index=False,sheet_name="spec自动化效率")
    writter.save()
    # Histogram(table_path,img_path)
if __name__ == '__main__':
    main()