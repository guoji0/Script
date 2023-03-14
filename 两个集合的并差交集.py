# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 00:06:17 2022

@author: guo
"""

nums1 = [4, 9, 5]
nums2 = [9,4,9,8,4]
print(list(set([i for i in nums1 if i in nums2])))
print(list(set(nums1).intersection(nums2)))


# 1. 获取两个list 的交集：

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
# 1
# 2
#方法一:

print([i for i in a if i in b])
# 1
# 结果： [3, 4]
#方法二，比方法一快很多！

print(set(a).intersection(b))
# 1
# 结果： {3， 4}

# 2. 获取两个list 的并集：

print(set(a).union(b))
# 1
# 结果：{1, 2, 3, 4, 5, 6}

# 3. 获取两个 list 的差集：

print(set(a).difference(b))  # a中有而b中没有的非常高效！
# 1
# 结果：{1, 2}

print(set(b).difference(a))  # b中有而a中没有1
# 结果：{5, 6}