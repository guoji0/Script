# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:52:50 2022

@author: guo

使用给定的整数n，编写程序以生成包含（i，i * i）的字典，该字典为1到n之间的整数。然后程序应打印字典。
"""


n = int(input())

adict = {}

for i in range(1,n+1):
    adict[i] = i*i
print(adict)