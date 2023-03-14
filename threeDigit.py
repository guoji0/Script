# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''
# a = [i for i in range(1,5)]
# b = []
# for i in a:
#     for x in a:
#         for y in a:
#             if i != x and i != y and x !=y:
#                 z = i*100 + x*10 +y
#                 b.append(z)
# c = len(b)
# print(c)
# print(b)
b = []
c = 0
def threeDigit(a):
    print(a)
    for i in a:
        for x in a:
            for y in a:
                if i != x and i != y and x !=y:
                    z = i*100 + x*10 +y
                    b.append(z)
    c = len(b)
    print(c)
    return b

if __name__ == '__main__':
    a = [i for i in range(1,5)]
    print(threeDigit(a))