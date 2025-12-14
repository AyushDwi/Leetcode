class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10**9 + 7
        
        seats = []
        for i, c in enumerate(corridor):
            if c == 'S':
                seats.append(i)
        
        if len(seats) < 2 or len(seats) % 2 == 1:
            return 0
        
        result = 1
        for i in range(1, len(seats) - 1, 2):
            gap = seats[i + 1] - seats[i]
            result = (result * gap) % MOD
        
        return result
