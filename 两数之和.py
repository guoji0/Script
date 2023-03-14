# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:49:12 2022

@author: guo
"""
# nums = [2,7,11,15]
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for idx,num in enumerate(nums):
            if target - num in d:
                return [d[target - num],idx]
            d[num] = idx
if __name__=='__main__':
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target))