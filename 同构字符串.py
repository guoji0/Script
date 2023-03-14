# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:34:31 2022

@author: guo
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def substr(astr):
            duplicate = ''
            ans = []
            for i in astr:
                if i in duplicate:
                    ans.append(duplicate.index(i))
                else:
                    duplicate += i
                    ans.append(duplicate.index(i))

            return ans
        return substr(s) == substr(t)

if __name__=='__main__':
    s = "abcdefghijklmnopqrstuvwxyzva"
    t = "abcdefghijklmnopqrstuvwxyzck"
    s1 = Solution()
    print(s1.isIsomorphic(s, t))
