"""The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn."""

class Solution:
    def tribonacci(self, n: int) -> int:
        

        if n < 3:
            return 1 if n else 0
        
        a = 1
        b = 1
        c = 2
        temp = c
        for _ in range(3, n):
            c = a + b + c
            a = b
            b = temp
            temp = c
            
        return c