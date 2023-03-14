# -*- coding: utf-8 -*-
"""
Created on Thu May 26 09:23:32 2022

@author: guo
"""
numRows = 6
class Solution:
    def generate(self, numRows: int):
        result = [[1]]
        for i in range(1,numRows):
            tmp1 = [0 for x in range(i+2)]
            tmp1[1:i+1] = result[i-1]
            tmp = [0 for j in range(i+1)]
            for j in range(i+1):
                tmp[j] = tmp1[j]+tmp1[j+1]
            result.append(tmp)
        return result