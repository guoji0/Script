# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:29:36 2022

@author: guo
"""
haystack = "hello"
needle = "ll"


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        if m == 0 or n == 0:
            return 0
        else:
            i = 0
            while i <= m - n:
                if haystack[i:i+n] == needle:
                    return i
                i += 1
            return -1