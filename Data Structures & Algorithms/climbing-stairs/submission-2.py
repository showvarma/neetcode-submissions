from math import comb
class Solution:
    def climbStairs(self, n: int) -> int:
        total = 0
        for y in range(n//2 +1):
            x= n - 2*y
            total += comb(x+y, y)
        return total


        