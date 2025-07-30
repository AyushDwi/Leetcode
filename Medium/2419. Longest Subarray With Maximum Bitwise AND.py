class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num=max(nums)
        current_len=0
        max_len=0
        for num in nums:
            if num==max_num:
                current_len+=1
                max_len=max(max_len,current_len)
            else:
                current_len=0
        return max_len            
        
