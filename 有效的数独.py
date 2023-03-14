# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:46:09 2022

@author: guo
"""
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                curr = board[i][j]
                if curr == '.':
                    continue
                box_index = i//3 * 3 + j//3
                if curr in row[i] or curr in col[j] or curr in box[box_index]:
                    return False
                
                row[i].add(curr)
                col[j].add(curr)
                box[box_index].add(curr)
        return True