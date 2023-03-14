# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 13:20:48 2022

@author: guo
"""
import math

# s = [1,2,3,4]
# s = [-2,1,-3,4,-1,2,1,-5,4]
s = [5,4,-1,7,8]

n = len(s)

if n == 0:
    print(0)
else:
    tmp = s[0]
    max_ = tmp
    for i in range(1,n):
        if tmp + s[i] > s[i]:
            print(max_)
            max_ = max(max_,tmp + s[i])
            tmp = tmp + s[i]
        else:
            max_ = max(max_,tmp,tmp + s[i],s[i])
            tmp = s[i]
    print(max_)