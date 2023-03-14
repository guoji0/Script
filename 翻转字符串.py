# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 20:43:02 2022

@author: guo
"""
s = ["h",'e']





class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        #适用于列表的所有长度类型
        n = len(s)

        for i in range(n//2):
            s[i],s[-i-1] = s[-i-1],s[i]
