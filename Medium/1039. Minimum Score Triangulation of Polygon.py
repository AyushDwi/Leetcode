class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        # Manual memoization using a dictionary
        memo = {}
        
        def dp(i, j):
            # Check if result is already cached
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: adjacent vertices form an edge, not a triangle
            if i + 1 == j:
                memo[(i, j)] = 0
                return 0
            
            min_score = float('inf')
            # Try all possible vertices k to form triangle (i, k, j)
            for k in range(i + 1, j):
                # Current triangle score + scores of left and right subproblems
                current_score = dp(i, k) + dp(k, j) + values[i] * values[k] * values[j]
                min_score = min(min_score, current_score)
            
            # Cache the result before returning
            memo[(i, j)] = min_score
            return min_score
        
        # Solve for the entire polygon from vertex 0 to n-1
        return dp(0, len(values) - 1)
