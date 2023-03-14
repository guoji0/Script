# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:21:22 2022

@author: guo
"""
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# words = ["d","do","dog","p","pe","pen","peng","pengu","pengui","penguin","e","el","ele","elep","eleph","elepha","elephan","elephant"]
words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
# words = ["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]
ans = ['']

# for index,item in enumerate(words):
#     n = len(item)
#     m = len(ans)
#     if item[:n-1] in words:
#         if n > m:
#             ans = item
#         if n <= m:
#             pass
#     else:
#         pass
# print(ans)


for w in words:
    n = len(w)
    for i in range(1,n+1):
        if w[:i] in words:
            pass 
        else:
            i = i -1
            break
    m1 = len(w[:i])
    m = len(ans[-1])
    if m1 > m:
        ans[:] = [w[:i]]
    elif m1 == m:
        ans.append(w[:i])
    else:
        pass
            
print(ans)
ans.sort()
