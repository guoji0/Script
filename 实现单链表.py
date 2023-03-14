# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:41:53 2022

@author: guo
"""
class Node(object):
    def __init__(self,elem):
        self.elem = elem 
        self.next = None
class singleLinkList(object):
    def __init__(self,node = None):
        self._head = node
    def is_empty(self):
        return self._head == None
    def length(self):
        cur = self._head 
        count = 0
        while cur != None:
            count += 1
            cur = cur.next 
        return count 
    def travel(self):
        cur = self._head 
        while cur != None:
            print(cur.elem)
            cur = cur.next
    def add(self,item):
        node = Node(item)
        node.next = self._head 
        self._head = node
                
    def append(self,item):
        node = Node(item)
        if self._head == None:
            self._head = node
        else:
            cur = self._head 
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self,pos,item):
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self._head 
            count = 0
            while count < (pos-1):
                cur = cur.next
                count += 1
                
            node.next = cur.next
            cur.next = node
            
    def remove(self,item):
        cur = self._head 
        pre = None
        while cur.next != None :
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next 
                
                
                
                
                
            
    def search(self,item):
        cur = self._head 
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
if __name__ == '__main__':
    sll = singleLinkList()
    # sll.append(1)
    # sll.add(5)
    # sll.append(1)
    # sll.append(1)
    # sll.append(1)
    # sll.insert(0, 9)
    # sll.remove(1)
    # sll.travel()
    # print(sll.search(5))
    
    # sll.append(1)
    # sll.append(2)
    # sll.append(2)
    # sll.append(1)
    # print(sll.travel())

