# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:25:32 2022

@author: guo
"""


def isValid(s):
    n = len(s)
    if n > 0:
        if n % 2 != 0:
            return False
        else:
            dict1 = {'(':1,')':-1,'{':2,'}':-2,'[':3,']':-3}
            s1 = ''
            for idx,it in enumerate(s):
                print(idx,it)
                if it in dict1.keys():
                    s1 += str(dict1[it])
            return s1
                    
                    

    else:
        return False
if __name__=='__main__':
    s = '()(){}'
    print(isValid(s))