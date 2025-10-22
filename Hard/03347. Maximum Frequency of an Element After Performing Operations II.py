class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        from collections import defaultdict
        cnt, d = defaultdict(int), defaultdict(int)
        for x in nums:
            cnt[x] += 1
            d[x], d[x-k], d[x+k+1] = d[x], d[x-k]+1, d[x+k+1]-1
        ans = s = 0
        for x in sorted(d):
            s += d[x]
            ans = max(ans, min(s, cnt[x] + numOperations))
        return ans
