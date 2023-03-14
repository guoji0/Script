# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:42:28 2022
1110101
@author: guo
"""
s = "0110"
n = len(s)
count = []
pre = cur = tmp = ans = 0
while cur < n:
    if s[pre] == s[cur]:
        tmp += 1
        cur += 1
    else:
        pre = cur
        count.append(tmp)
        tmp = 0
count.append(tmp)

for i in range(1,len(count)):
    ans += min(count[i-1:i+1])
print(ans)