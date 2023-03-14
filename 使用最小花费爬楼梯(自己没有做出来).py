# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 23:01:03 2022

@author: guo
"""
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])