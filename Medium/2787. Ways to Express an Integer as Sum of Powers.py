class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Step 1: Precompute powers
        powers = []
        base = 1
        p = base ** x
        while p <= n:
            powers.append(p)
            base += 1
            p = base ** x
        
        # Step 2: Memoization dictionary
        memo = {}
        
        # Step 3: DFS with memoization
        def dfs(remaining, idx):
            if remaining == 0:
                return 1
            if remaining < 0 or idx >= len(powers):
                return 0
            if (remaining, idx) in memo:
                return memo[(remaining, idx)]
            
            if powers[idx] > remaining:
                memo[(remaining, idx)] = dfs(remaining, idx + 1)
                return memo[(remaining, idx)]
            
            take = dfs(remaining - powers[idx], idx + 1)
            skip = dfs(remaining, idx + 1)
            
            memo[(remaining, idx)] = (take + skip) % MOD
            return memo[(remaining, idx)]
        
        return dfs(n, 0)
