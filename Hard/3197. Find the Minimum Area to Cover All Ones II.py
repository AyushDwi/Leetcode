class Solution(object):
    def minimumSum(self, grid):
        m, n = len(grid), len(grid[0])
        def get_rect_area(r1, r2, c1, c2):
            min_r, max_r = float('inf'), -1
            min_c, max_c = float('inf'), -1
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] == 1:
                        min_r = min(min_r, r)
                        max_r = max(max_r, r)
                        min_c = min(min_c, c)
                        max_c = max(max_c, c)
            if min_r == float('inf'):
                return 0
            return (max_r - min_r + 1) * (max_c - min_c + 1)
        def min_two_rects(r1, r2, c1, c2):
            min_area = float('inf')
            for cut_r in range(r1, r2):
                area1 = get_rect_area(r1, cut_r, c1, c2)
                area2 = get_rect_area(cut_r + 1, r2, c1, c2)
                if area1 > 0 and area2 > 0:
                    min_area = min(min_area, area1 + area2)
            for cut_c in range(c1, c2):
                area1 = get_rect_area(r1, r2, c1, cut_c)
                area2 = get_rect_area(r1, r2, cut_c + 1, c2)
                if area1 > 0 and area2 > 0:
                    min_area = min(min_area, area1 + area2)
            return min_area if min_area != float('inf') else 0
        min_total = float('inf')
        for cut_r in range(m - 1):
            top_area = get_rect_area(0, cut_r, 0, n - 1)
            bottom_two = min_two_rects(cut_r + 1, m - 1, 0, n - 1)
            if top_area > 0 and bottom_two > 0:
                min_total = min(min_total, top_area + bottom_two)
            bottom_area = get_rect_area(cut_r + 1, m - 1, 0, n - 1)
            top_two = min_two_rects(0, cut_r, 0, n - 1)
            if bottom_area > 0 and top_two > 0:
                min_total = min(min_total, bottom_area + top_two)
        for cut_c in range(n - 1):
            left_area = get_rect_area(0, m - 1, 0, cut_c)
            right_two = min_two_rects(0, m - 1, cut_c + 1, n - 1)
            if left_area > 0 and right_two > 0:
                min_total = min(min_total, left_area + right_two)
            right_area = get_rect_area(0, m - 1, cut_c + 1, n - 1)
            left_two = min_two_rects(0, m - 1, 0, cut_c)
            if right_area > 0 and left_two > 0:
                min_total = min(min_total, right_area + left_two)
        return min_total
        
