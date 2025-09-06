class Solution(object):
    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        def getOperations(n):
            if n <= 0:
                return 0
            
            result = 0
            operations = 0
            power_of_four = 1
            
            while power_of_four <= n:
                left = power_of_four
                right = min(n, power_of_four * 4 - 1)
                operations += 1
                
                result += (right - left + 1) * operations
                power_of_four *= 4
            
            return result
        
        total_operations = 0
        
        for l, r in queries:
            operations_for_range = getOperations(r) - getOperations(l - 1)
            total_operations += (operations_for_range + 1) // 2
        
        return total_operations
