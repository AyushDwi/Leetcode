class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        # Start with operations needed for first element
        operations = target[0]
        
        # For each subsequent element, add positive differences
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        
        return operations
