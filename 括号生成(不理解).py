# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 22:43:58 2022

@author: guo
"""
ans = []
n = 2
def backtrack(S, left, right):
    if len(S) == 2 * n:
        ans.append(''.join(S))
    if left < n: 
        print('left1:%d:'%left)
        S.append('(')
        backtrack(S, left+1, right)
        print('S1:%s' % S)
        # print('right:%d' %right)
        S.pop()
    
    print('left:%d' % left)
    if right < left:
        print('right1:%d' %right)
        S.append(')')
        backtrack(S, left, right+1)
        # print('left:%d:'%left)
        print('S2:%s' % S)
        S.pop()
    print('right:%d' % right)
backtrack([], 0, 0)