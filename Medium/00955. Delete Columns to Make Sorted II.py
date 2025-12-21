class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        deletions = 0
        unsorted = set(range(len(strs) - 1))
        
        for col in range(len(strs[0])):
            if any(strs[i][col] > strs[i + 1][col] for i in unsorted):
                deletions += 1
            else:
                unsorted -= {i for i in unsorted if strs[i][col] < strs[i + 1][col]}
        
        return deletions
