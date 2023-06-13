"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Basic Dynamic Programming
        """
        a = 1
        b = 2
        if n == 1 or n == 2:
            return n
        for i in range(2,n):
            b = a + b
            a = b - a
        
        return b