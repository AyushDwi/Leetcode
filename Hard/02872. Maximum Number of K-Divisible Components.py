import sys
sys.setrecursionlimit(100000)

class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        self.components = 0
        
        def dfs(node, parent):
            current_sum = values[node]
            
            for child in adj[node]:
                if child != parent:
                    current_sum += dfs(child, node)
            
            if current_sum % k == 0:
                self.components += 1
                return 0
            
            return current_sum
            
        dfs(0, -1)
        
        return self.components
