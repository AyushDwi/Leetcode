class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        dp = [1] * len(A[0])
        
        for i in range(len(A[0])-2, -1, -1):
            for j in range(i+1, len(A[0])):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], dp[j]+1)
        return len(A[0]) - max(dp)
