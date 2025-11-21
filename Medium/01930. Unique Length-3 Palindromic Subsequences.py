class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            left = s.find(c)
            right = s.rfind(c)
            
            if right - left > 1:
                result += len(set(s[left + 1:right]))
        
        return result
