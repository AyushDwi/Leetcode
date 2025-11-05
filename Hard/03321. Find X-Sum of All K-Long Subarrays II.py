from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        top = SortedList()  # (freq, num)
        remain = SortedList()  # (freq, num)
        freq = defaultdict(int)  # num -> freq
        cur_sum = 0
        
        def balance():
            """Balance between top and remain to keep top x elements"""
            nonlocal cur_sum
            
            # If top is smaller than x and remain has elements, move from remain to top
            if len(top) < x and remain:
                f, n = remain.pop()
                top.add((f, n))
                cur_sum += f * n
            
            # If top has more than x elements and the smallest in top is less than largest in remain
            if top and remain and top[0] < remain[-1]:
                f1, n1 = top.pop(0)
                f2, n2 = remain.pop()
                top.add((f2, n2))
                remain.add((f1, n1))
                cur_sum += (f2 * n2 - f1 * n1)
        
        def update(num, delta):
            """Update frequency of num by delta (+1 or -1)"""
            nonlocal cur_sum
            
            # Remove old entry if exists
            if num in freq:
                if (freq[num], num) in top:
                    top.remove((freq[num], num))
                    cur_sum -= freq[num] * num
                else:
                    remain.remove((freq[num], num))
            
            # Update frequency
            freq[num] += delta
            
            # Add new entry if frequency > 0
            if freq[num] == 0:
                del freq[num]
            else:
                remain.add((freq[num], num))
            
            # Balance to maintain top x
            balance()
        
        # Initialize with first k elements
        res = []
        for i in range(k):
            update(nums[i], 1)
        res.append(cur_sum)
        
        # Slide window
        for i in range(k, len(nums)):
            update(nums[i - k], -1)
            update(nums[i], 1)
            res.append(cur_sum)
        
        return res
