class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        k = 1
        while True:
            x = num1 - k * num2
            if x < 0:
                break
            if bin(x).count('1') <= k <= x:
                return k
            k += 1
        return -1
      
