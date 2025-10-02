class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # Start by drinking all initial bottles
        ans = numBottles
        
        # Keep exchanging while we have enough empty bottles
        while numBottles >= numExchange:
            # Exchange numExchange empties for 1 full bottle
            # After drinking: lose numExchange empties, gain 1 empty
            numBottles = numBottles - numExchange + 1
            
            # Increment exchange rate for next trade
            numExchange += 1
            
            # Add the newly obtained bottle to answer
            ans += 1
        
        return ans
