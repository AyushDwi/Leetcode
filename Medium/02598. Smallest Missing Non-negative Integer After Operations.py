class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        from collections import Counter
        
        # Count frequency of each remainder when dividing by value
        # Use (num % value) to handle both positive and negative numbers
        remainder_count = Counter(num % value for num in nums)
        
        # Try each integer starting from 0
        # We need at most len(nums) + 1 iterations
        for i in range(len(nums) + 1):
            # Check if we can form integer i
            # Integer i requires a number with remainder (i % value)
            if remainder_count[i % value] == 0:
                # No number available with the required remainder
                return i
            
            # Use one number with the required remainder to form integer i
            remainder_count[i % value] -= 1
        
        return len(nums)
