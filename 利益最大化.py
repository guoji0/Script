# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:06:16 2022

@author: guo
"""
nums = [7,1,5,3,6,4]
# nums = [7,6,4,3,1]
# nums = [1,2,4,6,8]
# nums = [6,1,3,2,4,7]
class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        t = 0 #总利润
        s,f = 0,1
        while f < n:
            if prices[s] <= prices[f]:
                t += prices[f] - prices[s]
            elif prices[s] > prices[f]:
                prices[s] = prices[f]
            s += 1
            f += 1
        return t
if __name__=='__main__':
    s = Solution()
    nums = [7,1,5,3,6,4]
    print(s.maxProfit(nums))