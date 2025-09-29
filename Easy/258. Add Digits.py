class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            temp=num
            sum_=0
            while temp!=0:
                sum_+=temp%10
                temp//=10
            num=sum_
        return num
