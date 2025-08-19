class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        current_zeros = 0
        
        for num in nums:
            if num == 0:
                current_zeros += 1
                total += current_zeros
            else:
                current_zeros = 0
        
        return total
