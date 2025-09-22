class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        max_freq = max(freq.values())
        return sum(f for f in freq.values() if f == max_freq)
