# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 13:52:22 2022

@author: guo
编写一个程序，该程序从控制台接受一个逗号分隔的数字序列，并生成一个列表和一个包含每个数字的元组
"""
astr = input()

alist = astr.split(',')
atuple = tuple(alist)

print(alist)
print(atuple)