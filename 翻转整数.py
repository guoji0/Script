# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:27:08 2022

@author: guo
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        ret = sign * int(str(abs(x))[::-1])
        if abs(ret) > 2 ** 31:
            ret = 0
        
        return ret