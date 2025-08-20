class Solution(object):
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp =  [0]* (cols + 1)
        total = 0
        
        for i in range(rows):
            prev_diag = 0
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i][j-1] == 1:
                    dp[j] = min(dp[j], dp[j-1], prev_diag) + 1
                    total += dp[j]
                else:
                    dp[j] = 0
                prev_diag = temp
        
        return total
        
