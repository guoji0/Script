# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:33:44 2022

@author: guo
"""

strs = ["flower","flow","flight"]
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n = min([len(i) for i in strs])
        s = ''
        result = ''
        for i in strs:
            if len(i) == n:
                s = i
                break
        i = 0
        while i < n:
            if list(s[i]) == list(set([n[i] for n in strs])):
                result += s[i]
            else:
                break
            i += 1

        return result