class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Sets to track which cells can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable, prev_height):
            # Check bounds, if already visited, or if height condition fails
            if (r, c) in reachable or r < 0 or r >= m or c < 0 or c >= n or heights[r][c] < prev_height:
                return
            
            # Mark as reachable
            reachable.add((r, c))
            
            # Explore all 4 directions
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, reachable, heights[r][c])
        
        # Start DFS from Pacific borders (top and left edges)
        for i in range(m):
            dfs(i, 0, pacific_reachable, heights[i][0])  # Left edge
        for j in range(n):
            dfs(0, j, pacific_reachable, heights[0][j])  # Top edge
        
        # Start DFS from Atlantic borders (bottom and right edges)  
        for i in range(m):
            dfs(i, n-1, atlantic_reachable, heights[i][n-1])  # Right edge
        for j in range(n):
            dfs(m-1, j, atlantic_reachable, heights[m-1][j])  # Bottom edge
        
        # Find intersection - cells that can reach both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])
        
        return result
