# -*- coding: utf-8 -*-
"""
Created on Sun May 22 22:23:22 2022

@author: guo
"""
prices = [7,1,5,3,6,4,1]
class Solution:
    def maxProfit(self, prices) -> int:
        # ans = [0]
        # low = prices[0]
        # n = len(prices)
        # for i in range(n):
        #     if prices[i] <= low:
        #         low = prices[i]
        #     else:
        #         ans.append(prices[i]-low)
        # return max(ans)
        
        ans = 0        
        n = len(prices)       
        dp = [0 for i in range(n+1)]
        dp[:n] = prices
        low = dp[0]
        for i in range(1,n+1):
            if dp[i] <= low:
                 low = dp[i]
                 ans = max(dp[i]-low,ans)
            else:
                ans = max(dp[i]-low,ans)
        return ans 
if __name__=='__main__':
    s = Solution()
    print(s.maxProfit(prices))
            