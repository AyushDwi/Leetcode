class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        row = len(grid) - 1
        col = 0
        
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                count += len(grid[0]) - col
                row -= 1
            else:
                col += 1
        
        return count
