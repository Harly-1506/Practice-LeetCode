"""The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,"""

#My solution
class Solution:
    def fib(self, n: int) -> int:

        if n == 0 or n == 1 or n == 5:
            return n
        if n == 2 or n == 3 or n == 4:
            return n - 1
        a = 3
        b = 5
        for i in range(5,n):
            b = a + b
            a = b - a
        return b