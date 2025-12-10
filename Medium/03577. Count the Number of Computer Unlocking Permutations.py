class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)
        
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        
        result = 1
        for i in range(1, n):
            result = (result * i) % MOD
        
        return result
