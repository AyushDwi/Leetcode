class Solution(object):
    def magicalSum(self, m, k, nums):
        """
        :type m: int
        :type k: int
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        def popcount(x):
            return bin(x).count('1')
        
        # Precompute factorials and inverse factorials
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i-1] * i % MOD
        
        inv_fact = [1] * (m + 1)
        inv_fact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        # Memoization cache
        memo = {}
        
        def dp(index, m_left, k_left, carry):
            # Base case: processed all indices
            if index == n:
                if m_left == 0 and k_left == popcount(carry):
                    return 1
                else:
                    return 0
            
            # Check cache
            state = (index, m_left, k_left, carry)
            if state in memo:
                return memo[state]
            
            # Early pruning
            if m_left < 0 or k_left < 0:
                memo[state] = 0
                return 0
            
            total = 0
            
            # Try using current index i times (0 to m_left)
            for i in range(m_left + 1):
                # Calculate new carry and bit contribution
                new_carry = (carry + i) // 2
                bit_contribution = (carry + i) % 2
                new_k_left = k_left - bit_contribution
                new_m_left = m_left - i
                
                # Recurse to next index
                ways = dp(index + 1, new_m_left, new_k_left, new_carry)
                
                if ways > 0:
                    if i > 0:
                        # Using this index i times
                        product_contrib = pow(nums[index], i, MOD)
                        coeff_contrib = inv_fact[i]  # 1/i! for multinomial coefficient
                        
                        contribution = product_contrib * coeff_contrib % MOD * ways % MOD
                        total = (total + contribution) % MOD
                    else:
                        # Not using this index at all
                        total = (total + ways) % MOD
            
            memo[state] = total
            return total
        
        # Start DP and multiply by m! at the end for total arrangements
        result = dp(0, m, k, 0)
        result = result * fact[m] % MOD
        
        return result
