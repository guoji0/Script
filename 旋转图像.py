# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:35:29 2022

@author: guo
"""
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        result = []
        for i in range(n):
            j = n - 1
            r = []
            while j > -1:
                r.append(matrix[j][i])
                j -= 1
            result.append(r)
        matrix[:] = result