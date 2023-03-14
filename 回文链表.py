# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:43:37 2022

@author: guo
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        ll = []
        while head:
            ll.append(head.val)
            head = head.next
        return ll == ll[::-1]