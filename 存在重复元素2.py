# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:30:34 2022

@author: guo
"""
nums = [1,0,1,1]
k = 1

ll = {}

for index,item in enumerate(nums):
    if item in ll and index - ll[item] <= k:
        print(True)
        break 
    ll[item] = index
print(False)