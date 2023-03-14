# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 11:46:24 2022

@author: guo
"""
# s = 'hello world'
# s = 'hello world'
s = '  fly me  to   the moon  '
# s = 'luffyisstilljoyboy'
s = s[::-1]
i = 0
while i < len(s):
    if s[i] == ' ':
        break
    else:
        pass
    i += 1
print(i)