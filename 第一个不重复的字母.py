# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:24:56 2022

@author: guo
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d ={}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for k in d:
            if d[k] != 1:
                continue
            else:
                return s.index(k)
        return -1
if __name__=='__main__':
    # s = 'loveleetcode'
    s = 'aabb'
    print(Solution().firstUniqChar(s))
