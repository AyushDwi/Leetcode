class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        stack = [0]
        
        for num in nums:
            while stack[-1] > num:
                stack.pop()
            
            if stack[-1] < num:
                count += 1
                stack.append(num)
        
        return count
