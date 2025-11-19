class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        
        while original in num_set:
            original <<= 1  # Left shift by 1 = multiply by 2
        
        return original
