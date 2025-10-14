class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        for start in range(n - 2*k + 1):
            # Check first subarray [start : start+k]
            first = nums[start : start + k]
            second = nums[start + k : start + 2*k]
            if self.isIncreasing(first) and self.isIncreasing(second):
                return True
        return False
    
    def isIncreasing(self, subarr):
        # Check strictly increasing
        for i in range(1, len(subarr)):
            if subarr[i] <= subarr[i-1]:
                return False
        return True
