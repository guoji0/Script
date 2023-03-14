# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:22:38 2022

@author: guo
"""
nums = [1,2,2,3,1,4,2]
dict1 = {}
for index,item in enumerate(nums):
    if item not in dict1:
        dict1[item] = [index]
    else:
        dict1[item].append(index)
ans = dict1[nums[0]]
for v in dict1.values():
    if len(v) == 1:
        pass
    else:
        if len(v) > len(ans):
            ans = v
        else:
            if len(v) == len(ans):
                if v[-1] -v[0] <= ans[-1] - ans[0]:
                    ans = v
                else:
                    pass
            else:
                pass
print(ans[-1] - ans[0] + 1)
                
                
                