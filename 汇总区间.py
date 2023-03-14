# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:51:22 2022

@author: guo
"""
nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
# nums = []
# nums = ""

n = len(nums)
ans = []
pre,cur = 0,1
while cur < n:
    if nums[cur] - nums[cur-1] == 1:        
        cur += 1
    else:
        tmp = cur
        ans.append(nums[pre:tmp])
        pre = cur 
        cur += 1
ans.append(nums[pre:cur])
print(ans)
result = []
for i in ans:
    if len(i) > 1:
        i = str(i[0])+'->'+str(i[-1])
    else:
        if i != [] and i != '':
            i = str(i[0])
        else:
            pass
print(ans)