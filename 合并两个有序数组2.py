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

        left = right = 0
        nums = []
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                nums.append(nums1[left]) 
                left += 1
            else:
                nums.append(nums2[right]) 
                right += 1
        while left < m:
            nums.append(nums1[left]) 
            left += 1
        
        while right < n:
            nums.append(nums2[right])
            right += 1
        
        nums1[:] = nums