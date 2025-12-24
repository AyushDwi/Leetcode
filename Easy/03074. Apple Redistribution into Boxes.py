class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        
        boxes_used = 0
        for cap in capacity:
            boxes_used += 1
            total_apples -= cap
            if total_apples <= 0:
                return boxes_used
        
        return boxes_used
