class Solution(object):
    def numberOfBeams(self, bank):
        ans = prev = 0
        for row in bank:
            curr = row.count('1')
            if curr:
                ans += prev * curr
                prev = curr
        return ans
