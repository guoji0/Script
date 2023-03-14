# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:14:00 2022

@author: guo
"""
# s = "-0042++.42"
# s = "-987words and 987"
s = "21474836460"


class Solution:
    def myAtoi(self, s: str) -> int:
        import re

        m = re.match(r'[-|+]?\d+',s.lstrip())


        if m :
            m = m.group()
            sign = -1 if '-' in m else 1          
            #return sign * abs(int(m)) if abs(int(m)) <= 2 ** 31 else sign * 2 ** 31
            if sign == 1:
                if abs(int(m)) > 2**31 -1:
                    return 2**31 -1
                else:
                    return abs(int(m))
            else:
                if abs(int(m)) > 2**31:
                    return -2**31
                else:
                    return -abs(int(m))
        else:
            return 0