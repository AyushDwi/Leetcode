class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 0.5
        
        # For large n, probability approaches 1.0 since A depletes much faster
        if n >= 4800:
            return 1.0
        
        # Memoization dictionary
        memo = {}
        
        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            # Four operations with equal probability
            prob = 0.25 * (
                dp(max(0, a - 100), b) +
                dp(max(0, a - 75), max(0, b - 25)) +
                dp(max(0, a - 50), max(0, b - 50)) +
                dp(max(0, a - 25), max(0, b - 75))
            )
            
            memo[(a, b)] = prob
            return prob
        
        return dp(n, n)
