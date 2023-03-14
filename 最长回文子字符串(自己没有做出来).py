# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:13:07 2022



babcbad
@author: guo
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.expandAroundCenter(s, i, i)
            s2 = self.expandAroundCenter(s, i, i + 1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]