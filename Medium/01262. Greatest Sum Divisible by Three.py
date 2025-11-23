class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            new_dp = dp[:]
            for j in range(3):
                remainder = (j + num) % 3
                new_dp[remainder] = max(new_dp[remainder], dp[j] + num)
            dp = new_dp
        
        return max(0, dp[0])
