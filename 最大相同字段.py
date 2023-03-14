# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:43:55 2022

@author: guo
"""
def returnstr (strs):
    min_len = ''
    i = 0
    s = ''

    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[-1]
    else:
        while i < len(strs) -1:
            if len(strs[i]) <= len(strs[i + 1]):
                min_len = strs[i]
            else:
                min_len = strs[i +1]
            i += 1
        for i in min_len:
            s += i
            for j in strs:
                if s == j[:len(s)]:
                    pass
                else:
                    return s[:-1]
        return s
if __name__=='__main__':
    strs = ['reflower','flow','flight']
    # strs = ['abca','aba','aaab']
    print(returnstr(strs))