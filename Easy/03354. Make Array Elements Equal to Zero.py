class Solution(object):
    def countValidSelections(self, nums):
        s = sum(nums)
        ans = l = 0
        for x in nums:
            if x:
                l += x
            else:
                r = s - l
                if l == r:
                    ans += 2
                elif abs(l - r) == 1:
                    ans += 1
        return ans
