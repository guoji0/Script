# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 13:56:13 2022

@author: guo
输出9*9口诀
"""
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'% (j,i,i*j),end= ' ')
    print()