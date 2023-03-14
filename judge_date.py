# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:24:16 2022

@author: guo

题目：输入某年某月某日，判断这一天是这一年的第几天？
"""

print('请输入年份:')


year = int(input())

print('请输入月份:')
month = int(input())

print('请输入日期:')
day = int(input())


bigMonth = [1,3,5,7,8,10,12]
smallMonth = [4,6,9,11]
dayInYear = 0
if (year % 4 ==0 and year % 100 !=0) or year % 400 == 0:
    febLength = 29
    day_big = 0
    day_small = 0
    if 1 <= month <= 2:
        dayInYear = (month -1) * 31 + day
    elif 12 >= month > 2:
        for m in range(1,month):
            if m in bigMonth:
                day_big += 31
            elif m in smallMonth:
                day_small += 30
        dayInYear = day_big + day_small + 29 + day
    else:
        print('输入有误!')
    print(dayInYear)
else:
    febLength = 28
    day_big = 0
    day_small = 0
    if 1 <= month <= 2:
        dayInYear = (month -1) * 31 + day
    elif 12 >= month > 2:
        for m in range(1,month):
            if m in bigMonth:
                day_big += 31
            elif m in smallMonth:
                day_small += 30
        dayInYear = day_big + day_small + day + 28
    else:
        print('输入有误!')
print('您输入的是%d的第%d天' % (year,dayInYear))


