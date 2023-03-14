# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 02:00:01 2022

@author: guo
"""
ops = ["5","-2","4","C","D","9","+","+"]
count = []
for o in ops:
    if o == 'C':
        count.pop()
    elif o == 'D':
        count.append(count[-1]*2)
    elif o == '+':
        count.append(count[-1]+count[-2])
    else:
        count.append(int(o))
print(count)
print(sum(count))