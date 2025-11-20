class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        result = 0
        s, e = -1, -1
        
        for a, b in intervals:
            if a <= s:
                continue
            if a > e:
                result += 2
                s, e = b - 1, b
            else:
                result += 1
                s, e = e, b
        
        return result
