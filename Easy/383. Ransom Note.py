class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Early termination optimization
        if len(ransomNote) > len(magazine):
            return False
        
        # Count characters in magazine
        char_count = {}
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Check if ransom note can be constructed
        for char in ransomNote:
            if char_count.get(char, 0) == 0:
                return False
            char_count[char] -= 1
        
        return True
