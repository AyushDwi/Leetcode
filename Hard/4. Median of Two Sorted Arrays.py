class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                nums.append(nums1[i])
                i=i+1
            elif nums1[i]>=nums2[j]:
                nums.append(nums2[j])
                j=j+1
        if i<len(nums1):
            nums.extend(nums1[i:])
        if j<len(nums2):
            nums.extend(nums2[j:])
            
        if len(nums)%2==1:
            return nums[len(nums)//2] 
        elif len(nums)%2==0:
            return float(nums[len(nums)//2] +nums[len(nums)//2 -1])/2                       
