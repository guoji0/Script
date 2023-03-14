# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 20:09:52 2022

@author: guo
"""
dict1 = {1:1,
         2:2,
         3:3,
         4:4,
         5:5,
         6:6,
         7:7,
         8:8,
         9:9,
         10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f'
         }
n = -2
ans = ''

if n <= -1:
    count = 1
    while n != -1:
        n,y = divmod(n, 16)
        if y == 0:
            ans += '0'
        else:
            ans += dict1[y]
        count += 1
    print((8-count)*'f'+ans[::-1])
            
else:
    while n != 0:    
    n,y = divmod(n, 16)
    if y == 0:
        ans += '0'
    else:
        ans += str(dict1[y])
        

    