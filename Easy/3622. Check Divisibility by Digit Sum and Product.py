class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum=0
        prod=1
        temp= n
    
        while temp:
            sum=sum+ temp%10
            prod*=temp%10
            temp//=10
        if n%(sum+prod)==0:
            return True 
        else :
            return False 
            
