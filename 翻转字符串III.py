# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:13:31 2022

@author: guo
"""
s = " Let's  take  LeetCode contest "
n  = len(s)
cur = pre = count = 0
ans = ''
while cur < n:
    if s[cur] != ' ':
        ans += count*' '
        count = 0
    else:
        ans += s[pre:cur][::-1]
        count += 1
        pre = cur
        pre += 1
    cur += 1
        
print(ans + s[pre:cur][::-1]+' '* count)
