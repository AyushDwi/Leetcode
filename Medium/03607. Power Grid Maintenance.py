class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        from sortedcontainers import SortedSet
        from collections import defaultdict
        
        # Union-Find
        parent = list(range(c + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # Build connected components
        for u, v in connections:
            union(u, v)
        
        # Map component root to sorted set of online stations
        component_stations = defaultdict(SortedSet)
        
        for station in range(1, c + 1):
            root = find(station)
            component_stations[root].add(station)
        
        result = []
        for query_type, x in queries:
            root = find(x)
            online = component_stations[root]
            
            if query_type == 1:
                # Maintenance check
                if x in online:
                    result.append(x)
                elif online:
                    result.append(online[0])  # Get minimum from sorted set
                else:
                    result.append(-1)
            else:
                # Take station offline
                online.discard(x)
        
        return result
