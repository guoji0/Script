# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 23:36:49 2022

@author: guo
"""
nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
# nums = [2, 1, -1]
n = len(nums)

num = [0 for i in range(n+2)]

num[1:n+1] = nums

# print(num)

count = sum(num)


for i in range(1,n+1):
    tmp = sum(num[:i])
    print(tmp)
    print(count - num[i])
    if tmp*2 == count - num[i]:
        print(i)
        break
    