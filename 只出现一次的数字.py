# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:18:14 2022

@author: guo
"""

class Solution:
    def singleNumber(self, nums):
        dict1 = dict(Counter(nums))
        for k,v in dict1.items():
            if v == 1:
                return k
if __name__=='__main__':
    from collections import Counter
    nums = [2,2,1]
    # nums = [4,1,2,1,2]
    print(Solution().singleNumber(nums))