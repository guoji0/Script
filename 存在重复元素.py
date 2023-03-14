# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:32:10 2022

@author: guo
"""


class Solution:
    def containsDuplicate(self, nums):
        nums1 = list(set(nums))
        if len(nums1) < len(nums):
            return False
        else:
            return True
if __name__=='__main__':
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))