class Solution:
    def maxOperations(self, s: str) -> int:
        ops = 0
        ones_count = 0
        i = 0
        
        while i < len(s):
            if s[i] == '1':
                ones_count += 1
                i += 1
            else:
                ops += ones_count
                while i < len(s) and s[i] == '0':
                    i += 1
        
        return ops
