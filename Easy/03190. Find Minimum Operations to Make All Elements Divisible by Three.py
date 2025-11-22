class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            remainder = num % 3
            if remainder != 0:
                result += min(remainder, 3 - remainder)
        return result
