class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        memo = {}
        
        def dfs(i, cur, t):
            # Base case: reached end of string
            if i >= n:
                return 1
            
            # Check memoization
            key = (i, cur, t)
            if key in memo:
                return memo[key]
            
            # Process current character without change
            v = 1 << (ord(s[i]) - ord('a'))  # Bit position for current char
            nxt = cur | v  # Add character to current set
            
            # Check if we exceed k distinct characters
            if bin(nxt).count('1') > k:
                # Start new partition
                ans = dfs(i + 1, v, t) + 1
            else:
                # Continue current partition
                ans = dfs(i + 1, nxt, t)
            
            # Try changing current character (if allowed)
            if t:
                for j in range(26):
                    nxt = cur | (1 << j)  # Try adding character 'a' + j
                    if bin(nxt).count('1') > k:
                        # Changing forces new partition
                        ans = max(ans, dfs(i + 1, 1 << j, 0) + 1)
                    else:
                        # Continue with changed character
                        ans = max(ans, dfs(i + 1, nxt, 0))
            
            memo[key] = ans
            return ans
        
        return dfs(0, 0, 1)
