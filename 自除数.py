# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:28:46 2022

@author: guo
"""
left ,right = 1, 22

ans = []

for num  in range(left,right+1):
    if '0' not in num:
        nums = [int(i) for i in str(num) if i != '0' and num % int(i) != 0]
        
        if len(nums) == 0:
            ans.append(num)
return ans 


print([int(i) for i in str(100) if i != '0'])