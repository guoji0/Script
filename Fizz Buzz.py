# -*- coding: utf-8 -*-
"""
Created on Thu May 26 23:11:22 2022

@author: guo
"""
class Solution:
    def fizzBuzz(self, n: int):
        ans = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 != 0 and i % 15 != 0:
                ans.append('Fizz')
            elif i % 5 == 0 and i % 15 != 0:
                ans.append('Buzz')
            elif i % 15 == 0 :
                ans.append('FizzBuzz')
            else:
                ans.append(str(i))
        return ans
if __name__=='__main__':
    s = Solution()
    print(s.fizzBuzz(3))