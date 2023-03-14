# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:05:16 2022

@author: guo
"""

nums = [3,0,1]


for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] >= nums[j]:
            nums[i],nums[j] = nums[j],nums[i]


class Solution:
    def missingNumber(self, nums) -> int:
        #return [j for j in range(len(nums) + 1) if j not in nums][-1]
        #return list(set(j for j in range(len(nums)+1)) - set(nums))[-1]
        return sum([i for i in range(len(nums)+1)]) - sum(nums)

