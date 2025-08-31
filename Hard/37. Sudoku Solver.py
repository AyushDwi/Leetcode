class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]
        empty_cells = []
        
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    digit = ord(board[i][j]) - ord('1')  
                    box_idx = (i // 3) * 3 + (j // 3)
                    rows[i][digit] = True
                    cols[j][digit] = True
                    boxes[box_idx][digit] = True
        
        def backtrack(idx):
            
            if idx == len(empty_cells):
                return True
            
            row, col = empty_cells[idx]
            box_idx = (row // 3) * 3 + (col // 3)
            
            
            for digit in range(9):
                if not rows[row][digit] and not cols[col][digit] and not boxes[box_idx][digit]:
                    
                    board[row][col] = chr(digit + ord('1'))
                    rows[row][digit] = True
                    cols[col][digit] = True
                    boxes[box_idx][digit] = True
                    
                    
                    if backtrack(idx + 1):
                        return True
                    
                    
                    board[row][col] = '.'
                    rows[row][digit] = False
                    cols[col][digit] = False
                    boxes[box_idx][digit] = False
            
            return False
        
        backtrack(0)
