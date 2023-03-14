# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:51:46 2022

@author: guo
"""
s = "   fly me   to   the moon  "
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(' ')[-1]
        return len(s)