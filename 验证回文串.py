# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:32:36 2022

@author: guo
"""
# s ="A man, a plan, a canal: Panama"
# s ="race a car"
s ="0P"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ''
        result = []
        for i in s:
            if i.isalnum():
                m += i.lower()                
        if len(m) >= 0:            
            for i in range(len(m)//2):
                if m[i] != m[~i]:
                    result.append(False)
                else:
                    continue
            return False if False in result else True 
        return False


