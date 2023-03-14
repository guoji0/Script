# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:55:59 2022

@author: guo
"""
# 100



l,r = 1,n

while l < r:
    mid = (l+r) // 2
    if mid == False:
        l = mid + 1
    else:
        r = mid - 1
return l

