# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:32:42 2022

@author: guo
"""
# upper = 0
# lower = 0
# word = "FlaG"
# n = len(word)
# for w in word:
#     if w.isupper():
#         upper += 1        
#     else:
#         lower += 1
# if upper == n or lower == n or (word[0].isupper() and upper == 1):
#     return True
# else:
#     return False



a = "aba"
b = "cdc"
la = len(a)
lb = len(b)

if la != lb:
    return la if la > lb else lb
else:
    count = 0
    