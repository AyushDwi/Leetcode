class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0           # Maximum k found so far
        pre = 0           # Length of previous strictly increasing sequence
        cur = 0           # Length of current strictly increasing sequence
        n = len(nums)
        
        for i in range(n):
            cur += 1      # Increment current sequence length
            
            # Check if we've reached the end of an increasing sequence
            # (either at last element or next element is not greater)
            if i == n - 1 or nums[i] >= nums[i + 1]:
                # Update answer considering two cases:
                # 1. Split current sequence into two equal parts: cur // 2
                # 2. Use previous and current adjacent sequences: min(pre, cur)
                ans = max(ans, cur // 2, min(pre, cur))
                
                # Update previous length and reset current
                pre = cur
                cur = 0
        
        return ans
