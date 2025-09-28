class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=0         
        n=len(digits)
        for i in range(-1,-(n)-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            elif digits[i]==9 :
                digits[i]=0
                carry+=1
        
        if carry==n:
            digits=[1]+digits
        return digits    


                   




