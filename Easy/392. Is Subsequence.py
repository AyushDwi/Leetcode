class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        if s[-1]==t[-1]:
            return self.isSubsequence(s[:-1],t[:-1])
        return self.isSubsequence(s,t[:-1])           
        
