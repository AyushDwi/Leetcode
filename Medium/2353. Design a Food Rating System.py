import heapq
from collections import defaultdict

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        # Map food name to (rating, cuisine) for O(1) lookup
        self.food_info = {}
        
        # Map cuisine to heap of (-rating, food_name) 
        # Using negative rating to simulate max heap since Python heapq is min heap
        self.cuisine_heaps = defaultdict(list)
        
        # Initialize data structures
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            
            # Store food info for quick lookup
            self.food_info[food] = [rating, cuisine]
            
            # Add to cuisine heap with negative rating for max heap behavior
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        # Get current cuisine
        old_rating, cuisine = self.food_info[food]
        
        # Update food info
        self.food_info[food][0] = newRating
        
        # Add new entry to heap (lazy deletion approach)
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.cuisine_heaps[cuisine]
        
        # Remove outdated entries from top of heap
        while heap:
            neg_rating, food = heap[0]
            current_rating = self.food_info[food][0]
            
            # If the rating matches, this is the current highest rated food
            if -neg_rating == current_rating:
                return food
            
            # Otherwise, this entry is outdated, remove it
            heapq.heappop(heap)
        
        return ""  # Should never reach here based on problem constraints
