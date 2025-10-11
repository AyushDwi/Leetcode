class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        from collections import Counter
        import bisect
        
        # Count frequency of each damage value
        count = Counter(power)
        
        # Get unique damage values and sort them
        unique_damages = sorted(count.keys())
        
        n = len(unique_damages)
        if n == 0:
            return 0
        
        # dp[i] represents the maximum damage we can get using damages[0..i]
        dp = [0] * n
        
        for i in range(n):
            current_damage = unique_damages[i]
            current_total = current_damage * count[current_damage]
            
            if i == 0:
                dp[i] = current_total
            else:
                # Option 1: Don't use current damage
                dp[i] = dp[i-1]
                
                # Option 2: Use current damage
                # Binary search for the rightmost position with damage < current_damage - 2
                target = current_damage - 2
                j = bisect.bisect_left(unique_damages, target) - 1
                
                if j >= 0:
                    dp[i] = max(dp[i], dp[j] + current_total)
                else:
                    dp[i] = max(dp[i], current_total)
        
        return dp[n-1]
