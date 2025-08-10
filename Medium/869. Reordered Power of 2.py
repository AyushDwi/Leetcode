from collections import Counter

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cntn = Counter(str(n))
        # check powers of 2 up to 2^29 (since n ≤ 10^9)
        for i in range(30):
            if cntn == Counter(str(1 << i)):
                return True
        return False
