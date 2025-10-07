import bisect

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        result = [-1] * n  # Initialize with -1 (for rainy days)
        
        # Track available sunny days (when rains[i] == 0)
        sunny_days = []  # Sorted list of indices where we can dry lakes
        
        # Track when each lake was last filled
        lake_to_last_rain = {}
        
        for i in range(n):
            if rains[i] == 0:
                # Sunny day - add to available days
                sunny_days.append(i)
                result[i] = 1  # Temporary placeholder (will be updated if needed)
            else:
                # Rainy day - check if this lake is already full
                lake = rains[i]
                
                if lake in lake_to_last_rain:
                    # Lake is already full, need to find a sunny day to dry it
                    last_rain_day = lake_to_last_rain[lake]
                    
                    # Find first sunny day after the last rain on this lake
                    # Use binary search to find the first sunny day > last_rain_day
                    pos = bisect.bisect_right(sunny_days, last_rain_day)
                    
                    if pos == len(sunny_days):
                        # No sunny day available after last rain - impossible to avoid flood
                        return []
                    
                    # Use this sunny day to dry the lake
                    dry_day = sunny_days[pos]
                    result[dry_day] = lake
                    
                    # Remove this sunny day as it's now used
                    sunny_days.pop(pos)
                
                # Update when this lake was last filled
                lake_to_last_rain[lake] = i
        
        return result
