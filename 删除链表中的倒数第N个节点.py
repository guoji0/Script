# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:49:38 2022

@author: guo
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummyNode = ListNode(0)
        dummyNode.next = head
        cur = dummyNode 
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        
        cur = dummyNode
        for i in range(count - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummyNode.next