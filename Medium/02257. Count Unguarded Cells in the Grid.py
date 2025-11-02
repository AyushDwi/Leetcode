class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        # Create grid: 0=empty, 1=guarded, 2=guard, 3=wall
        grid = [[0] * n for _ in range(m)]
        
        # Mark guards as 2
        for r, c in guards:
            grid[r][c] = 2
        
        # Mark walls as 3
        for r, c in walls:
            grid[r][c] = 3
        
        # Mark cells guarded by each guard (4 directions)
        def dfs(row, col, dr, dc):
            # Move in one direction until hitting wall or guard
            row += dr
            col += dc
            
            while 0 <= row < m and 0 <= col < n and grid[row][col] != 2 and grid[row][col] != 3:
                grid[row][col] = 1  # Mark as guarded
                row += dr
                col += dc
        
        # For each guard, mark all cells it can see
        for r, c in guards:
            dfs(r, c, -1, 0)  # Up
            dfs(r, c, 1, 0)   # Down
            dfs(r, c, 0, -1)  # Left
            dfs(r, c, 0, 1)   # Right
        
        # Count unoccupied and unguarded cells (value = 0)
        count = 0
        for row in grid:
            count += row.count(0)
        
        return count
