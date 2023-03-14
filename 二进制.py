# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:12:54 2022

@author: guo
"""
s1 = '11'
s2 = '11'
a = [i for i in s1[::-1]]
b = [i for i in s2[::-1]]
na = len(a)
nb = len(b)
s = []
sf = ''
if na > nb:
    
    for i in range(na):
        if i <= nb - 1:
            s.append(str(int(a[i]) + int(b(i))))
        else:
            s.append(a[i])
else:
    for i in range(nb):
        if i <= na - 1:
            s.append(str(int(a[i]) + int(b[i])))
        else:
            s.append(b[i])
print(s)
i = 0
while i < len(s) - 1:
    if int(s[i]) < 2:
        s[i] = s[i]
    else:
        s[i] = str(int(s[i]) - 2)
        s[i+1] = str(int(s[i+1]) + 1)
    i += 1
if int(s[-1]) >= 2:
    s[-1] = str(int(s[-1]) - 2)
    s.append('1')
else:
    s[-1] = s[-1]
print(''.join(s[::-1]))
    