class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        prev = [[0] * k for _ in range(n + 1)]
        prev[1][0] = 1
        
        for i in range(m):
            curr = [[0] * k for _ in range(n + 1)]
            for j in range(n):
                for r in range(k):
                    new_r = (r + grid[i][j]) % k
                    curr[j + 1][new_r] = (
                        curr[j + 1][new_r] + 
                        prev[j + 1][r] + 
                        curr[j][r]
                    ) % MOD
            prev = curr
        
        return prev[n][0]
