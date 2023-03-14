# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:08:16 2022

@author: guo
"""
def num(n):
    if n == 0:
        return 1
    else:
        return n*num(n-1)
n = 5
s = 0
if n % 2 == 1:
    for i in range(0,(n+1)//2):
        if i == 0:
            s = s + 1
        else:
            s = s + num(n-2*i)/num(n-3*i)
else:
    for i in range(0,(n+2)//2):
        if i == 0 or 2 * i ==n:
            s = s + 1
        else :
            s = s + num(n)/num(n-i)
print(s)


