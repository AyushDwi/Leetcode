class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # Start by drinking all initial bottles
        total_drunk = numBottles
        empty_bottles = numBottles  # After drinking, we have this many empties
        
        # Keep exchanging while we have enough empty bottles
        while empty_bottles >= numExchange:
            # Calculate how many new bottles we can get
            new_bottles = empty_bottles // numExchange
            
            # Add to total drunk count
            total_drunk += new_bottles
            
            # Update empty bottles count:
            # - Remove the ones we used for exchange
            # - Add the new empties from drinking the new bottles
            empty_bottles = empty_bottles % numExchange + new_bottles
        
        return total_drunk
