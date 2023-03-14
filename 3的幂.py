# -*- coding: utf-8 -*-
"""
Created on Thu May 26 22:40:37 2022

@author: guo
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        nums = [3**i for i in range(32)]
        if n in nums:
            return True
        else:
            return False