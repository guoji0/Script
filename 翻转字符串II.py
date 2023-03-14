# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 09:32:57 2022

@author: guo
"""
def reverseStr(s,k):
    n = len(s)
    z,y = divmod(n,k)
    count = 0
    ans = ''
    if k >= n:
        return s[::-1]
    else:
        for i in range(1,z+1):
            if i % 2 == 1:
                ans += s[count:count+k][::-1]
                count += k
            else:
                ans += s[count:count+k]
                count += k
        return ans+s[count:] if z % 2 == 1 else ans+s[count:][::-1]
if __name__ == '__main__':
    s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
    print(len(s))
    k = 39
    print(reverseStr(s, k))
    