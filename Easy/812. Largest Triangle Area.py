class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0.0
        
        # Check all possible combinations of three points using brute force
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    # Get coordinates of the three points
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    
                    # Calculate area using the cross product formula
                    # Area = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
                    
                    # Update maximum area if current area is larger
                    max_area = max(max_area, area)
        
        return max_area
