class Solution(object):
    def climbStairs(self, x):
        if x <= 2:
            return x
        a, b = 1, 2
        for _ in range(3, x + 1):
            a, b = b, a + b
        return b
