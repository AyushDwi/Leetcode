import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def gain(p, t):
            return (t - p) / (t * float(t + 1))
        
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        total = 0.0
        for _, p, t in heap:
            total += p / float(t)
        return total / float(len(classes))
      
