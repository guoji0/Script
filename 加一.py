# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:17:48 2022

@author: guo
"""
class Solution:
    def plusOne(self, digits):
        num = str(int(''.join(map(str,digits))) + 1)
        if num[-1] != 0:            
            return [int(i) for i in num]
        else:
            return [int(i) for i in num.pop()]
if __name__=='__main__':
    digits = []
    print(Solution().plusOne(digits))