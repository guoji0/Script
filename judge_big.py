# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:23:00 2022

@author: guo


输入三个整数x,y,z，请把这三个数由小到大输出
"""
print('请输入第一个整数:')
x = int(input())
print('请输入第二个整数:')
y = int(input())
print('请输入第三个整数:')
z = int(input())

# alist = [2,8,9,5,20,35,84,11,3,98]
alist = []
alist.append(x)
alist.append(y)
alist.append(z)
# print(sorted(alist,reverse=False))

for i in range(len(alist)-1):
    for j in range(i+1,len(alist)):
        min_digit = 0
        if alist[i] >= alist[j]:
            min_digit = alist[i]
            alist[i] = alist[j]
            alist[j] = min_digit
print(alist)
print(','.join(alist))