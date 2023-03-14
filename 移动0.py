# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:42:15 2022

@author: guo
"""

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        s,f = 0,0
        while f < n:
            if nums[f] != 0:
                cur = nums[s]
                nums[s] = nums[f]
                nums[f] = cur
                s += 1
            f += 1
        return nums
if __name__== '__main__':
    # nums = [0,1,0,3,12,0,1]
    # nums = [1,0,0,3,12,0,1]
    # nums = [0]
    nums = [1,0]
    print(Solution().moveZeroes(nums))
