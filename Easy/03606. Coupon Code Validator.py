class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        def is_valid_code(s):
            if not s:
                return False
            for c in s:
                if not (c.isalnum() or c == '_'):
                    return False
            return True
        
        valid_business_lines = {'electronics', 'grocery', 'pharmacy', 'restaurant'}
        
        valid_indices = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in valid_business_lines and is_valid_code(code[i]):
                valid_indices.append(i)
        
        valid_indices.sort(key=lambda i: (businessLine[i], code[i]))
        
        return [code[i] for i in valid_indices]
