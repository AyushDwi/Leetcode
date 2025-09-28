class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(n>9):
            temp=n
            sqsum=0
            while(temp!=0):
                sqsum+=(temp%10)*(temp%10)
                temp//=10
                n=sqsum

        if n==1 or n==7:
            return True
        else:
            return False            

