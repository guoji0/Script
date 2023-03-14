# -*- coding: utf-8 -*-
"""
Created on Sun May 22 22:12:50 2022

@author: guo
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = {1:1,2:2}
        for i in range(3,n+1):
            ans[i] = ans[i-1]+ans[i-2]
        return ans[n]