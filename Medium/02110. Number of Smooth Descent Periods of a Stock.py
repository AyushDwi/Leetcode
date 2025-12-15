class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count = 0
        current_length = 1
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                current_length += 1
            else:
                count += current_length * (current_length + 1) // 2
                current_length = 1
        
        count += current_length * (current_length + 1) // 2
        return count
