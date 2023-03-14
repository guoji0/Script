# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:23:53 2022

@author: guo
"""
nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2,1,-3,4]
# nums = [5,4,-1,7,8]
# nums = [1]
n = len(nums)
result = -int(1e9)
count = 0
for i in range(n):
    count += nums[i]
    if count > result:
        result = count
    if count <= 0:
        count = 0
print(result)
        




# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # 定义prev用于存储当前元素之前的最大值
#         prev = 0
#         # 初始化结果变量
#         res = -int(1e9)
#         # 遍历数组
#         for li in nums:
#             # 每次更新当前元素及其之前的最大值，这里可以拿实例手动推导一下，会发现跟前面的推导
#             # 流程是一样的，这里的max(prev+li, li)就是实现了每次考虑是否加上前面的最大值，但是
#             # 同时还需要加上二者之间的元素，比如遍历到4，前面最大的元素是1， 由于上一步遍历到-3
#             # 时，最大值是1-3=-2，所以此时的prev是-2，那显然max(-2+4, 4)结果为4
#             prev = max(prev+li, li)
#             # 更新最大结果
#             res = max(res, res+prev)
#         return res
