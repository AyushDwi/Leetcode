class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        n = high - low + 1  # Total numbers in range
        
        if n % 2 == 0:
            return n // 2
        else:
            return n // 2 + (1 if low % 2 != 0 else 0)
