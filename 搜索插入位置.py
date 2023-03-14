# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:43:17 2022

@author: guo
"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if target <= nums[i]:
                return i
            else:
                i += 1
        return n 