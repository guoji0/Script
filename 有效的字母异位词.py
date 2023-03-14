# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:11:08 2022

@author: guo
# """
# s = "anagram"
# t = "nagaram"
# print(len(s))
# print(len(t))
s = "rat"
t = "car"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == len(t):
            ds = {}
            dt = {}
            result = []
            for i in s:
                if i not in ds:
                    ds[i] = 1
                else:
                    ds[i] += 1
            for i in t:
                if i not in dt:
                    dt[i] = 1
                else:
                    dt[i] += 1
            
            for m in ds:
                if m not in dt or dt[m] != ds[m]:
                    result.append(False)
                else:
                    continue
            return False if len(result) >= 1 else True 
        else:
            return False