# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:37:23 2022

@author: guo
"""
'''
题目：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
'''
import math
print(math.sqrt(9))
def return_num():
    for a in range(0,269):
        for b in range(0,269):
            if (a-b)*(a+b) == 268 and a >= b:
                return (a,b)
print(return_num()[0])
c = math.pow(return_num()[0], 2) - 368
print(c)
            