import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Add all boundary cells to the heap
        # Top and bottom rows
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[0][j] = True
            visited[m-1][j] = True
        
        # Left and right columns (excluding corners already added)
        for i in range(1, m-1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][0] = True
            visited[i][n-1] = True
        
        water = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
        
        while heap:
            height, x, y = heapq.heappop(heap)
            
            # Check all four neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Skip if out of bounds or already visited
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                    continue
                
                visited[nx][ny] = True
                
                # Calculate trapped water at this neighbor
                water += max(0, height - heightMap[nx][ny])
                
                # Add neighbor to heap with updated height
                # The new height is at least as high as current height
                heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return water
