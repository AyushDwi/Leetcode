class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        from collections import defaultdict
        
        cnt = defaultdict(int)
        
        d = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            d[x] += 0
            d[x - k] += 1      
            d[x + k + 1] -= 1 
        ans = 0
        current = 0  
        for x in sorted(d.keys()):
            current += d[x]
            ans = max(ans, min(current, cnt[x] + numOperations))
        
        return ans
