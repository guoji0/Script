# -*- coding: utf-8 -*-
"""
Created on Thu May  5 21:50:42 2022

@author: guo
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val = node.next.val
            node.next = node.next.next
        node.val = node.next.val
        node.next = None                