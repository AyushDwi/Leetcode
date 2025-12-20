class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        deletions = 0
        num_cols = len(strs[0])
        
        for col in range(num_cols):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    deletions += 1
                    break
        
        return deletions
