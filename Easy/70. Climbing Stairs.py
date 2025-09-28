class Solution(object):
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n):
        if n <= 3:
            return n
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
