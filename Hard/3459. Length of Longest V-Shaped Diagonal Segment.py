class Solution:
    def lenOfVDiagonal(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        next_val = {1: 2, 2: 0, 0: 2}
        dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        dp = [[[0] * 4 for _ in range(n)] for _ in range(m)]
        
        for d, (dr, dc) in enumerate(dirs):
            if dr == 1 and dc == 1:
                for r in range(m-1, -1, -1):
                    for c in range(n-1, -1, -1):
                        self._fill_dp(grid, dp, r, c, d, dr, dc, next_val, m, n)
            elif dr == 1 and dc == -1:
                for r in range(m-1, -1, -1):
                    for c in range(n):
                        self._fill_dp(grid, dp, r, c, d, dr, dc, next_val, m, n)
            elif dr == -1 and dc == 1:
                for r in range(m):
                    for c in range(n-1, -1, -1):
                        self._fill_dp(grid, dp, r, c, d, dr, dc, next_val, m, n)
            else:
                for r in range(m):
                    for c in range(n):
                        self._fill_dp(grid, dp, r, c, d, dr, dc, next_val, m, n)
        
        max_len = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 1:
                    continue
                
                for d in range(4):
                    max_len = max(max_len, dp[r][c][d])
                
                for d1 in range(4):
                    dr1, dc1 = dirs[d1]
                    turn_dr, turn_dc = dc1, -dr1
                    d2 = self._get_direction_index(dirs, turn_dr, turn_dc)
                    if d2 == -1:
                        continue
                    curr_r, curr_c = r, c
                    first_arm_len = dp[r][c][d1]
                    for step in range(1, first_arm_len):
                        curr_r += dr1
                        curr_c += dc1
                        if not (0 <= curr_r < m and 0 <= curr_c < n):
                            break
                        second_arm_len = dp[curr_r][curr_c][d2]
                        if second_arm_len > 1:
                            v_len = step + 1 + second_arm_len - 1
                            max_len = max(max_len, v_len)
        
        return max_len
    
    def _fill_dp(self, grid, dp, r, c, d, dr, dc, next_val, m, n):
        curr_val = grid[r][c]
        if curr_val not in next_val:
            dp[r][c][d] = 1
            return
        
        nr, nc = r + dr, c + dc
        if (0 <= nr < m and 0 <= nc < n and grid[nr][nc] == next_val[curr_val]):
            dp[r][c][d] = 1 + dp[nr][nc][d]
        else:
            dp[r][c][d] = 1
    
    def _get_direction_index(self, dirs, dr, dc):
        for i, (d_r, d_c) in enumerate(dirs):
            if d_r == dr and d_c == dc:
                return i
        return -1
