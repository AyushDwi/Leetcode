class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total_cost = 0
        i = 0
        
        while i < len(colors):
            
            j = i
            while j < len(colors) and colors[j] == colors[i]:
                j += 1
            
            
            if j - i > 1:
                
                group = neededTime[i:j]
                total_cost += sum(group) - max(group)
            
           
            i = j
        
        return total_cost
