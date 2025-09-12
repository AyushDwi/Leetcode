class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiou')
        
        
        for char in s:
            if char in vowels:
                return True
        
     
        return False
      
