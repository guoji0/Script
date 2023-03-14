# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:21:42 2022

@author: guo
"""
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0 and n != 0:
            nums1[:] = nums2 
        elif m != 0 and n == 0:
            pass
        else:
            nums = nums1[:m] + nums2[:n]
            for i in range(m+n):
                for j in range(i,m+n):
                    if nums[i] <= nums[j]:
                        pass
                    else:
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
            nums1[:] = nums

                    
                    