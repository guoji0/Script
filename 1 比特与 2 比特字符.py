# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:03:27 2022

@author: guo
"""
bits = [1,1,1,0]
n = len(bits)

i = 0
while i < n-1:
    if bits[i] == 0:
        i += 1
    else:
        i += 2
print(True if i == n-1 else False)