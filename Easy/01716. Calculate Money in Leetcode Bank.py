class Solution(object):
    def totalMoney(self, n):
        w, d = divmod(n, 7)
        return (28 + 28 + 7 * (w - 1)) * w // 2 + (w * 2 + d + 1) * d // 2
