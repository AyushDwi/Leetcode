class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        nums.sort()
        left=0
        right=len(nums)-1
        while left<right:
            sum=sum+nums[right-1]
            right=right-2
            left=left+1
        return sum    
       
