class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """

        # Step 1: Create frequency maps
        from collections import Counter
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        total_freq = Counter()

        min_elem = float('inf')

        # Step 2: Build total_freq and find global minimum element
        for fruit in basket1 + basket2:
            total_freq[fruit] += 1
            min_elem = min(min_elem, fruit)

        # Step 3: Check for impossibility
        for fruit in total_freq:
            if total_freq[fruit] % 2 != 0:
                return -1

        # Step 4: Build excess lists
        extra1 = []
        extra2 = []

        for fruit in total_freq:
            half = total_freq[fruit] // 2
            if freq1[fruit] > half:
                extra1.extend([fruit] * (freq1[fruit] - half))
            if freq2[fruit] > half:
                extra2.extend([fruit] * (freq2[fruit] - half))

        # Step 5: Sort extras to minimize cost
        extra1.sort()
        extra2.sort(reverse=True)

        # Step 6: Calculate total cost
        cost = 0
        for a, b in zip(extra1, extra2):
            cost += min(min(a, b), 2 * min_elem)

        return cost
