# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:39:26 2022

@author: guo
"""
# nums = [1,2,3,4,5,6,7]
# nums = [5,6,7,1,2,3,4]
nums = [-1,-100,3,99]
print(nums[:])
# k = 2

# n = len(nums)
# m = k % n


# nums1 = (nums[n-m:] + nums[:n-m])
# nums = nums1
# print(nums)
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = k % n
        nums[:] = (nums[n-m:] + nums[:n-m])
if __name__=='__main__':
    nums = [1,2,3,4,5,6,7]
    k = 2
    print(Solution().rotate(nums, 2))