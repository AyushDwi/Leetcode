class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from math import gcd
        
        n = len(nums)
        
        
        ones_count = nums.count(1)
        if ones_count > 0:
            return n - ones_count
        
       
        min_length = n + 1
        
        for i in range(n):
            current_gcd = 0
            
            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])
                
                if current_gcd == 1:
                    min_length = min(min_length, j - i + 1)
                    break
        
    
        if min_length > n:
            return -1
        
       
        return n + min_length - 2
