class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sort array to process elements from smallest to largest
        nums.sort()
        
        distinct_count = 0
        previous_value = float('-inf')  # Track last assigned value
        
        for num in nums:
            # Calculate optimal value for current element
            # Range for this element: [num - k, num + k]
            
            # We want the smallest value that is:
            # 1. Greater than previous_value (for distinctness)
            # 2. Within the allowed range [num - k, num + k]
            
            current_value = min(num + k, max(num - k, previous_value + 1))
            
            # Check if we can assign a distinct value
            if current_value > previous_value:
                distinct_count += 1
                previous_value = current_value
        
        return distinct_count
