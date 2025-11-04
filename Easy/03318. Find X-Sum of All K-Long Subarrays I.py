class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        result = []
        
        # Process each k-length subarray
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i+k]
            
            # Count frequencies
            freq = {}
            for num in subarray:
                freq[num] = freq.get(num, 0) + 1
            
            
            items = [(num, count) for num, count in freq.items()]
            items.sort(key=lambda p: (p[1], p[0]), reverse=True)
            
            
            x_sum = 0
            for j in range(min(x, len(items))):
                value, count = items[j]
                x_sum += value * count
            
            result.append(x_sum)
        
        return result
