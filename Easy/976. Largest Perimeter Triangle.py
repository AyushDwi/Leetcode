class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort array in ascending order
        nums.sort()
        
        # Check from largest to smallest possible triangles
        # Start from end and work backwards
        for i in range(len(nums) - 1, 1, -1):
            # Get three consecutive elements (sorted)
            largest = nums[i]
            middle = nums[i - 1] 
            smallest = nums[i - 2]
            
            # Check triangle inequality: sum of two smaller > largest
            if smallest + middle > largest:
                return smallest + middle + largest
        
        # No valid triangle found
        return 0
