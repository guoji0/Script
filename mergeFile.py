# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:35:33 2022

@author: guo
"""
import os

filename_list = []
for filename in os.listdir(r'C:\Users\86150\Desktop\工作\文档'):
    if len(filename.split('.')[0]) == 4:
        
        filename_list.append(filename)
print(filename_list)