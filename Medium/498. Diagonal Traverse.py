class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        up = True

        for d in range(m + n - 1):
            start_row = max(0, d - (n - 1))
            end_row = min(d, m - 1)

            if up:
                r = end_row
                while r >= start_row:
                    c = d - r
                    result.append(mat[r][c])
                    r -= 1
            else:
                r = start_row
                while r <= end_row:
                    c = d - r
                    result.append(mat[r][c])
                    r += 1

            up = not up

        return result
