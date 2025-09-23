class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Split both versions by '.' to get individual revision numbers
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        
        # Get the maximum length to compare all parts
        max_length = max(len(v1_parts), len(v2_parts))
        
        # Compare each revision number from left to right
        for i in range(max_length):
            # Get the revision number or 0 if it doesn't exist
            num1 = int(v1_parts[i]) if i < len(v1_parts) else 0
            num2 = int(v2_parts[i]) if i < len(v2_parts) else 0
            
            # Compare the revision numbers
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        
        # All revision numbers are equal
        return 0
