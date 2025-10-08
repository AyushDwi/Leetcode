class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_={}
        res=0
        for i in s:
            if i not in hash_:
                hash_[i]=1
            elif i in hash_:
                hash_[i]+=1
                if hash_[i]%2==0:
                    res+=2

        odd=0        
        for i in hash_:
            if hash_[i]%2==1:
                odd=1
                break
        return res+odd            
