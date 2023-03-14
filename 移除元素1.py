# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:09:17 2022

@author: guo
"""
nums = [3,2,2,3]
nums = [0,1,2,2,3,0,4,2]
nums = [2,2,3,3]
class Solution:
    def removeElement(self, nums, val: int) -> int:
        cur = pre = count = 0
        n = len(nums)
        while cur < n:
            if nums[cur] != val:
                nums[pre],nums[cur] = nums[cur],nums[pre]
                cur += 1
                pre += 1
            else:
                cur += 1
                count += 1
        nums[:] = nums[:n-count]