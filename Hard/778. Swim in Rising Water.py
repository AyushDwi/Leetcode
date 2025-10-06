import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        # Dijkstra's algorithm approach
        # We want to find the path with minimum "maximum elevation"
        visited = set()
        # Priority queue: (max_elevation_so_far, row, col)
        pq = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            max_elevation, row, col = heapq.heappop(pq)
            
            # If we've already visited this cell, skip
            if (row, col) in visited:
                continue
                
            # Mark as visited
            visited.add((row, col))
            
            # If we reached the destination
            if row == n - 1 and col == n - 1:
                return max_elevation
            
            # Explore all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and if already visited
                if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                    # The elevation for this path is the max of current path elevation and new cell elevation
                    new_elevation = max(max_elevation, grid[new_row][new_col])
                    heapq.heappush(pq, (new_elevation, new_row, new_col))
        
        return -1  # Should never reach here for valid input
