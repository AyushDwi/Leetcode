class Solution(object):
    def subarrayBitwiseORs(self, arr):
        All_ORs = set()      # Set to store all distinct bitwise OR results
        prev = set()         # Set of ORs of subarrays ending at previous element

        for num in arr:
            curr = set()     # Set of ORs of subarrays ending at current element

            curr.add(num)    # Every new element starts a new subarray by itself

            for val in prev:
                curr.add(val | num)  # Extend each previous subarray by OR-ing with current element

            All_ORs.update(curr)     # Add all OR results from current position to global result set
            prev = curr              # Update prev to be current for the next iteration

        return len(All_ORs)          # Return the number of unique OR results
