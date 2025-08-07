class Solution(object):
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        total = sum(fruits[i][i] for i in range(n))
        dp2 = [[-1] * n for _ in range(n)]

        def dfs2(row, col):
            if row == n - 1:
                return fruits[n-1][n-1] if col == n-1 else float('-inf')
            if dp2[row][col] != -1:
                return dp2[row][col]
            result = float('-inf')
            for dc in [-1, 0, 1]:
                new_col = col + dc
                if 0 <= new_col < n:
                    current = fruits[row][col] if row != col else 0
                    result = max(result, current + dfs2(row + 1, new_col))
            dp2[row][col] = result
            return result

        dp3 = [[-1] * n for _ in range(n)]

        def dfs3(row, col):
            if col == n - 1:
                return fruits[n-1][n-1] if row == n-1 else float('-inf')
            if dp3[row][col] != -1:
                return dp3[row][col]
            result = float('-inf')
            for dr in [-1, 0, 1]:
                new_row = row + dr
                if 0 <= new_row < n:
                    current = fruits[row][col] if row != col else 0
                    result = max(result, current + dfs3(new_row, col + 1))
            dp3[row][col] = result
            return result

        child2_max = dfs2(0, n - 1)
        child3_max = dfs3(n - 1, 0)
        return total + child2_max + child3_max - 2 * fruits[n-1][n-1]
