class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Process the array layer by layer, reducing size by 1 each iteration
        for current_length in range(len(nums) - 1, 0, -1):
            # For each position in current layer, sum adjacent elements
            for i in range(current_length):
                # Replace current element with sum of itself and next element, mod 10
                nums[i] = (nums[i] + nums[i + 1]) % 10
        
        # Return the final remaining element
        return nums[0]
