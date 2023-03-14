# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 00:01:19 2022

@author: guo
"""
letters = ["c", "f", "j"]
target = "c"
letters.append(target)
letter = list(set(letters))
letter.sort()
print(letter)
if target == letters[-1]:
    print(letters[0])
elif target == letters[0]:
    print(letters[1])
else:
    print(letters[letters.index(target)+1])