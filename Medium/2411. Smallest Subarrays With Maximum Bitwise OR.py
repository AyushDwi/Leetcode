class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        last_seen = [-1] * 32  # last index where bit i was seen

        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if (nums[i] >> bit) & 1:
                    last_seen[bit] = i

            max_index = i
            for bit in range(32):
                if last_seen[bit] != -1:
                    max_index = max(max_index, last_seen[bit])

            answer[i] = max_index - i + 1

        return answer
