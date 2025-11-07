class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # First, figure out how much power each city gets from existing stations
        # A station at position i covers cities from max(0, i-r) to min(i+r, n-1)
        # Using a difference array to efficiently compute this
        change = [0] * (n + 1)
        for i in range(n):
            start = max(0, i - r)
            end = min(i + r, n - 1)
            change[start] += stations[i]
            change[end + 1] -= stations[i]
        
        # Convert the difference array to actual power values
        current_power = 0
        city_power = []
        for i in range(n):
            current_power += change[i]
            city_power.append(current_power)
        
        # Now we need to find the maximum possible minimum power
        # Key insight: if we can achieve minimum power X, we can achieve any Y < X
        # So we binary search on the answer
        
        def can_reach(min_power):
            # Check if we can make all cities have at least min_power
            # with k additional power stations
            
            stations_left = k
            extra_power = [0] * (n + 1)  # track additional power from new stations
            extra = 0  # running sum of extra power
            
            for idx in range(n):
                extra += extra_power[idx]
                
                total = city_power[idx] + extra
                shortage = min_power - total
                
                if shortage > 0:
                    # This city doesn't have enough power
                    if stations_left < shortage:
                        return False  # can't fix it
                    
                    # Add stations. Where should we place them?
                    # Place them as far right as possible while still covering this city
                    # This helps the next cities too
                    rightmost_pos = min(idx + r, n - 1)
                    
                    # These stations will cover from (rightmost_pos - r) to (rightmost_pos + r)
                    cover_start = max(0, rightmost_pos - r)
                    cover_end = min(rightmost_pos + r, n - 1)
                    
                    extra_power[cover_start] += shortage
                    extra_power[cover_end + 1] -= shortage
                    extra += shortage
                    stations_left -= shortage
            
            return True
        
        # Binary search for the answer
        answer = 0
        low, high = 0, sum(stations) + k
        
        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                answer = mid
                low = mid + 1  # try to get higher
            else:
                high = mid - 1  # too high, go lower
        
        return answer
