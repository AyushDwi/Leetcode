import itertools

class Solution(object):
    def judgePoint24(self, cards):
        EPS = 1e-6

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    a, b = nums[i], nums[j]
                    remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    candidates = [
                        a + b,
                        a * b,
                        a - b,
                        b - a
                    ]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)
                    for candidate in candidates:
                        if solve(remaining + [candidate]):
                            return True
            return False

        nums = [float(x) for x in cards]
        return solve(nums)
