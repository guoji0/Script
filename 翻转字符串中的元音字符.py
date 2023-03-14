# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 23:09:50 2022

@author: guo
"""
s = "leetcode"
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u']
        n = len(s)
        vowel_list = []
        ans = [0 for i in range(n)]
        for index,item in enumerate(s):
            if item.lower() in vowel:
                vowel_list.append(item)
            else:
                ans[index] = item
        for i in range(n):
            if ans[i] == 0:
                ans[i] = vowel_list.pop()
            else:
                pass
        return ''.join(ans)
    
