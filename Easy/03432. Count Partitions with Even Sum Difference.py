class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0
