# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:41:39 2022

@author: guo

编写一个程序，可以计算给定数字的阶乘。结果应以逗号分隔的顺序打印在一行上。

"""
print('请输入一个整数:')
anum = int(input())
if anum > 0:
    jiecheng = 1
    for i in range(1,anum+1):
        jiecheng *= i
    print('%d的阶乘是%d' % (anum,jiecheng))
else:
    print('0和负数没有阶乘')
