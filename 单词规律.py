# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 23:45:05 2022

@author: guo
"""
def substr(pattern):
    duplicate = []
    ans = []
    for i in pattern:
        if i in duplicate:
            ans.append(duplicate.index(i))
        else:
            duplicate.append(i)
            ans.append(duplicate.index(i))

    return ans
def substr1(s):
    duplicate = []
    ans = []
    astr = s.split(' ')
    for i in astr:
        if i in duplicate:
            ans.append(duplicate.index(i))
        else:
            duplicate.append(i)
            ans.append(duplicate.index(i))

    return ans
pattern = "abba"
s = "dog cat cat dog"
print(s.split(' '))
print(substr(pattern))
print(substr1(s))
