class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        from collections import deque
        
        # Initialize BFS
        queue = deque([s])
        visited = {s}
        result = s
        
        while queue:
            current = queue.popleft()
            
            # Update result if current string is lexicographically smaller
            if current < result:
                result = current
            
            # Operation 1: Add 'a' to all odd-indexed digits (modulo 10)
            add_operation = ''.join(
                str((int(ch) + a) % 10) if i % 2 == 1 else ch
                for i, ch in enumerate(current)
            )
            
            # Operation 2: Rotate string right by 'b' positions
            rotate_operation = current[-b:] + current[:-b]
            
            # Add both transformations to queue if not visited
            for transformed in [add_operation, rotate_operation]:
                if transformed not in visited:
                    visited.add(transformed)
                    queue.append(transformed)
        
        return result
