# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:02:56 2022

@author: guo
"""
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]

pre = -10**4

res = nums[0]

for num in nums:
    pre = max(num,pre+num)
    res = max(res,pre)
print(res)