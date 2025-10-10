class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        dp = energy[:]  # Copy the array
        
        # Work backwards to build up the maximum energy from each position
        for i in range(n - 1 - k, -1, -1):
            dp[i] += dp[i + k]
        
        return max(dp)
