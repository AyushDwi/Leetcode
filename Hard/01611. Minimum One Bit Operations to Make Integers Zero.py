class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        from math import log2
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(x):
            if x == 0:
                return 0
            
            # Find the highest set bit position
            bit_pos = int(log2(x))
            # f(x) = 2^(b+1) - 1 - f(x - 2^b)
            return (1 << (bit_pos + 1)) - 1 - dp(x - (1 << bit_pos))
        
        return dp(n)
