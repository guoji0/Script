# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 21:18:15 2022

@author: guo
"""

from collections import Counter
licensePlate = "GrC8950"


result = ans = alpha = ''
for l in licensePlate:
    if l.isalpha():
        alpha += l.lower()

words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]

for word in words:
    for w in word:
        if w.lower() in alpha:
            ans += w.lower()
    for a in ans:
        if ans.count(a) < alpha.count(a):
            break
            word = ''
        else:
            continue
    if word == '':
        pass 
    else:       
        if result == '':
            result = word
        else:
            if len(word) < len(result):
                result = word
            else:
                pass
    ans = ''
print(result)
