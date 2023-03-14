# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:19:35 2022

@author: guo
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        cur = head
        pre = None
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur 
            cur = temp
        return pre