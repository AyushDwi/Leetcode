class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        
        result = [words[0]]
        
        for i in range(1, len(words)):
            # If sorted characters are different, they're not anagrams
            if sorted(words[i-1]) != sorted(words[i]):
                result.append(words[i])
        
        return result
