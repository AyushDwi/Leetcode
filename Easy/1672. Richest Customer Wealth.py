class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_=0
        for i in range(0,len(accounts)):
            if sum(accounts[i])>max_:
                max_=sum(accounts[i])
        return max_        

        
