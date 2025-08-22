class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        min_row, max_row = m, -1
        min_col, max_col = n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i < min_row:
                        min_row = i
                    if i > max_row:
                        max_row = i
                    if j < min_col:
                        min_col = j
                    if j > max_col:
                        max_col = j

        if max_row == -1:
            return 0

        height = max_row - min_row + 1
        width = max_col - min_col + 1

        return height * width
