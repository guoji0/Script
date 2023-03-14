# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:49:00 2022

@author: guo
"""
one = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M': 1000}
two = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

s = "MCMXCIV"
s = "LVIII"


n = len(s)

i = 0

count = 0

while i < n:
    if s[i:i+2] in two:
        count += two[s[i:i+2]]
        i += 2
    else:
        count += one[s[i]]
        i += 1
    print(i)
print(count)