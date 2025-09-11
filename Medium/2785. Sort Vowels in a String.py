class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = [c for c in s if c in "aeiouAEIOU"]
        vowels.sort()
        result = []
        vowel_idx = 0
        
        for c in s:
            if c in "aeiouAEIOU":
                result.append(vowels[vowel_idx])
                vowel_idx += 1
            else:
                result.append(c)
        
        return ''.join(result)
      
