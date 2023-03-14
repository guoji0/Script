# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:49:20 2022

@author: guo
"""
class Solution:
    def removeDuplicates(nums):
        n = len(nums)
        if n == 0 or n == 1:
            return n
        else:
            i , l = 1, 1
            cur = nums[0]
            while l < n:
                if cur !=  nums[l]:
                    nums[i] = nums[l]
                    cur = nums[i]
                    i += 1
                l += 1
            return i
    if __name__=='__main__':
        nums = [0,0,1,1,2,2,3]
        print(removeDuplicates(nums))     
        