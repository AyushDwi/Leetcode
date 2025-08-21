class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        res = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] else 0
            res += self.countHistogram(heights)
        return res

    def countHistogram(self, heights):
        n = len(heights)
        stack = []
        res = 0
        sum_arr = [0] * n
        for j in range(n):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            if stack:
                prev = stack[-1]
                sum_arr[j] = sum_arr[prev] + heights[j] * (j - prev)
            else:
                sum_arr[j] = heights[j] * (j + 1)
            res += sum_arr[j]
            stack.append(j)
        return res
        
        
