class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        s = [0] * (n + 1)
        t = [0] * (n + 1)
        
        for i in range(1, n + 1):
            s[i] = s[i - 1] + prices[i - 1] * strategy[i - 1]
            t[i] = t[i - 1] + prices[i - 1]
        
        ans = s[n]
        
        for i in range(k, n + 1):
            profit = s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k // 2])
            ans = max(ans, profit)
        
        return ans
