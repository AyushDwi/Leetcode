class Solution:
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pts = points
        n = len(pts)
        pts.sort(key=lambda p: (p[0], -p[1]))

        ans = 0
        ys = [p[1] for p in pts]

        for i in range(n - 1):
            yi = ys[i]
            max_y = -10**9
            local_ys = ys
            local_ans = ans
            for yj in local_ys[i+1:]:
                if yj <= yi and yj > max_y:
                    max_y = yj
                    local_ans += 1
            ans = local_ans

        return ans
