from bisect import bisect_left, bisect_right

class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        pos = [f[0] for f in fruits]
        pre = [0]
        for f in fruits: pre.append(pre[-1] + f[1])

        def total(l, r):
            i, j = bisect_left(pos, l), bisect_right(pos, r)
            return pre[j] - pre[i]

        res = 0
        for d in range(k + 1):
            if k - 2 * d >= 0:
                res = max(res, total(startPos - d, startPos + (k - 2 * d)))
            if k - 2 * d >= 0:
                res = max(res, total(startPos - (k - 2 * d), startPos + d))
        return res
