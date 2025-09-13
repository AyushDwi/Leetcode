class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        
        rows = [[] for _ in range(numRows)]
        
        
        current_row = 0
        direction = -1  # -1 for up, 1 for down
        
        
        for char in s:
            
            rows[current_row].append(char)
            
            
            if current_row == 0 or current_row == numRows - 1:
                direction = -direction
            
            
            current_row += direction
        
        
        return ''.join(''.join(row) for row in rows)
      
