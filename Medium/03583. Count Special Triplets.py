class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        result = 0
        
        left_count = {}
        right_count = {}
        
        for num in nums:
            right_count[num] = right_count.get(num, 0) + 1
        
        for j in range(n):
            right_count[nums[j]] -= 1
            if right_count[nums[j]] == 0:
                del right_count[nums[j]]
            
            target = nums[j] * 2
            triplet_count = (left_count.get(target, 0) * right_count.get(target, 0)) % MOD
            result = (result + triplet_count) % MOD
            
            left_count[nums[j]] = left_count.get(nums[j], 0) + 1
        
        return result
