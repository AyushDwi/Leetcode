class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Work with absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        
        # Calculate remainder
        remainder = numerator % denominator
        
        # If no remainder, return integer result
        if remainder == 0:
            return "".join(result)
        
        # Add decimal point
        result.append(".")
        
        # Track remainders and their positions for cycle detection
        remainder_map = {}
        
        while remainder != 0:
            # If remainder is seen before, we found a cycle
            if remainder in remainder_map:
                # Insert opening parenthesis at the start of cycle
                index = remainder_map[remainder]
                result.insert(index, "(")
                result.append(")")
                break
            
            # Record remainder position
            remainder_map[remainder] = len(result)
            
            # Perform long division
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)
