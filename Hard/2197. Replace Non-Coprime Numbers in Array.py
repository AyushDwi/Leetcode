class Solution(object):
    def gcd(self, a, b):
        """Calculate GCD using Euclidean algorithm"""
        while b:
            a, b = b, a % b
        return a
    
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for num in nums:
            stack.append(num)
            
            # Keep checking if we can merge the top two elements
            while len(stack) > 1:
                # Get the last two elements
                second_last = stack[-2]
                last = stack[-1]
                
                # Calculate GCD using our custom function
                gcd_val = self.gcd(second_last, last)
                
                # If they are coprime (GCD = 1), break
                if gcd_val == 1:
                    break
                
                # They are non-coprime, calculate LCM and merge
                lcm = (second_last * last) // gcd_val
                
                # Remove both elements and add their LCM
                stack.pop()  # Remove last
                stack[-1] = lcm  # Replace second_last with LCM
        
        return stack
