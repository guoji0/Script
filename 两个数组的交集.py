# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:51:04 2022

@author: guo
"""
nums1 = [1,2,2,1,3]
nums2 = [2,2,2,0]


tmp =list(set([val for val in nums1 if val in nums2]))

result = []
for i in tmp:
    result += [i]*min(nums1.count(i),nums2.count(i))
print(result)
