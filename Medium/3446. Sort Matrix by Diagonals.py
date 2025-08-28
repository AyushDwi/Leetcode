import collections, heapq

class Solution(object):
    def sortMatrix(self, grid):
        m, n = len(grid), len(grid[0])
        diag_map = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                k = i - j
                if k >= 0:
                    heapq.heappush(diag_map[k], -grid[i][j])
                else:
                    heapq.heappush(diag_map[k], grid[i][j])
        for i in range(m):
            for j in range(n):
                k = i - j
                if k >= 0:
                    grid[i][j] = -heapq.heappop(diag_map[k])
                else:
                    grid[i][j] = heapq.heappop(diag_map[k])
        return grid
