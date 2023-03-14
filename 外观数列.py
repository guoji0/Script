# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:28:57 2022

@author: guo
"""
# class Solution:
#     def countAndSay(self, n: int) -> str:
n = 5    
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        if n == 1:
            pass
        else:
            for i in range(1,n):
                
                count = 0
                element = s[0]
                ans = ''
                for j in range(len(s)):            
                    if s[j] == element:
                        print('element0:%s' % element)
                        count += 1

                    else:
                        print('element1:%s' % element)
                        ans = ans + str(count) + element
                        element = s[j]
                        count = 1
                ans = ans + str(count) + element
                s = ans
        return s
                
