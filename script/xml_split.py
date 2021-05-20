from xml.dom import minidom as minidom
from xml.dom import  Node
import pandas as pd
import datetime
#import numpy as np
'''text = 'Extra Header Start\
Extra Header End\
Extra Header Start\
Extra Header End'
with open('/home/guo/script/tscancode202105121758.xml') as lines:
    f = lines.readlines()
    if text in f:
        text=''
    lines.close()'''
print('请输入要处理的文件路径：')
file_name = input()
csv_header = ['file','line','id','subid','severity','msg','web_identify','func_info','content']

doc=minidom.parse(file_name) #先把xml文件加载进来
                   
root=doc.documentElement#解析根元素
print(root.nodeName,',',root.nodeValue,',',root.nodeType)               #获取元素的根节点
errors=root.getElementsByTagName('error')
total_list = []
if errors :
    for error in errors:
        alist = []        
        '''print('文件名是：%s'% error.getAttribute('file'))
        print('报错行是：%s'% error.getAttribute('line'))
        print('错误大类是：%s'% error.getAttribute('id'))
        print('错误小类是：%s'% error.getAttribute('subid'))
        print('错误级别：%s'% error.getAttribute('severity'))
        print('错误信息：%s'% error.getAttribute('msg'))
        print('网络标识：%s'% error.getAttribute('web_identify'))
        print('出错方法：%s'% error.getAttribute('func_info'))
        print('内容：%s'% error.getAttribute('content'))'''
        alist.append(error.getAttribute('file'))
        alist.append(error.getAttribute('line'))
        alist.append(error.getAttribute('id'))
        alist.append(error.getAttribute('subid'))
        alist.append(error.getAttribute('severity'))
        alist.append(error.getAttribute('msg'))
        alist.append(error.getAttribute('web_identify'))
        alist.append(error.getAttribute('func_info'))
        alist.append(error.getAttribute('content'))
        total_list.append(alist)
    #print(total_list)
    #print(total_list[2])
    df = pd.DataFrame(total_list, columns=csv_header)
    df.to_excel('Tscancode_'+datetime.datetime.now().strftime("%Y%m%d%H%M")+'.xlsx', index=None)
    print('文件处理完成！')
else:
    print('文件为空，请核实！')




