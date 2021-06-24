from xml.dom import minidom as minidom
from xml.dom import  Node
import os
import pandas as pd
import datetime


print('请输入要处理的文件路径：')
file_name = input()
csv_header = ['file','line','column','severity','id','msg','verbose','cwe','info']

doc=minidom.parse(file_name) #先把xml文件加载进来
print("xmldom.parse:", type(doc))
                   
root=doc.documentElement#解析根元素
print ("domobj.documentElement:", type(root))
print(root.nodeName,',',root.nodeValue,',',root.nodeType) #获取元素的根节点
errors=root.getElementsByTagName('error')
total_list = []
if errors :
    for error in errors:
        alist = []
        locations=error.getElementsByTagName('location')
        print('报错等级：%s'% error.getAttribute('severity'))
        print('错误类型：%s'% error.getAttribute('id'))
        print('报错短信息：%s'% error.getAttribute('msg'))
        print('报错长信息：%s'% error.getAttribute('verbose'))
        print('报错id：%s'% error.getAttribute('cwe'))
        
        line_list=[]
        column_list=[]
        info_list=[]
        for location in locations:
            line_list.append(location.getAttribute('line'))
            column_list.append(location.getAttribute('column'))
            info_list.append(location.getAttribute('info'))        
        print('出错文件行：%s'% location.getAttribute('file'))
        print('出错文件行：%s'% '||'.join(line_list))
        print('出错文件列：%s'% '||'.join(column_list))
        print('错误信息：%s'% '||'.join(info_list))
        alist.append(location.getAttribute('file'))
        alist.append('||'.join(line_list))
        alist.append('||'.join(column_list))
        alist.append(error.getAttribute('severity'))
        alist.append(error.getAttribute('id'))
        alist.append(error.getAttribute('msg'))
        alist.append(error.getAttribute('verbose'))
        alist.append(error.getAttribute('cwe'))
        alist.append('||'.join(info_list))        
        total_list.append(alist)
    df = pd.DataFrame(total_list, columns=csv_header)
    df.to_excel('cppcheck_'+datetime.datetime.now().strftime("%Y%m%d%H%M")+'.xlsx', index=None)
    print('文件处理完成！')
else:
    print('文件为空，请核实！')




