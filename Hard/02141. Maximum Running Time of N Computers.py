class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def can_run(time):
            return sum(min(b, time) for b in batteries) >= n * time
        
        left, right = 0, sum(batteries)
        while left < right:
            mid = (left + right + 1) // 2
            if can_run(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
