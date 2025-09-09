class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        # Circular buffer for dp values of the past `forget` days
        dp = [0] * forget
        dp[0] = 1  # Day 1 (index 0)
        
        sharing = 0
        for day in range(1, n):
            # index in circular buffer for today
            idx = day % forget
            
            # Remove the value from the day that just exited the window
            sharing = (sharing - dp[idx] + MOD) % MOD
            
            # Add those who start sharing today
            if day >= delay:
                sharing = (sharing + dp[(day - delay) % forget]) % MOD
            
            # Record number who discover today
            dp[idx] = sharing
        
        # Sum up those who still remember (last forget days)
        result = sum(dp[(n - 1 - i) % forget] for i in range(min(n, forget))) % MOD
        return result
      
