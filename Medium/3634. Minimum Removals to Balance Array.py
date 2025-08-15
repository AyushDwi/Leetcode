class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        left=0
        mbl=0

        for right in range(n):
            while nums[right]>nums[left]*k:
                left+=1
            cl=right-left+1
            mbl=max(mbl,cl)
        return n-mbl    
            
        
