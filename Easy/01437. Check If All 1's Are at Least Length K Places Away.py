class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one = -float('inf')
        
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - prev_one - 1 < k:
                    return False
                prev_one = i
        
        return True
